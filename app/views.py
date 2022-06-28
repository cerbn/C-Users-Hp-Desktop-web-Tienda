from email.headerregistry import Group
from multiprocessing.sharedctypes import Value
from re import A
from unicodedata import name
import requests
from django.shortcuts import redirect, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from app.forms import ProductoForm
from .forms import *
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login
# Create your views here.


def index(request):
    response = requests.get('https://digimon-api.herokuapp.com/api/digimon').json()
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll,
        'listajson' : response  }

    return render(request, 'app/index.html', datos)



def perrito(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }   
    return render(request, 'app/perrito.html', datos)
    

def gato(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }    
    return render(request, 'app/gato.html', datos)

def pajaros(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }    
    return render(request, 'app/pajaros.html', datos)

def suscripcion(request):
    return render(request, 'app/Suscripcion.html')

def ayuda(request):
    return render(request, 'app/paginaAyuda.html')

def todos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }    
    return render(request, 'app/todos.html', datos)

def registro(request):
    return render(request, 'app/registro.html')
    
def conf_pago(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()
    return render(request, 'app/conf_pago.html')


@login_required
def usuario_iniciado(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.stock = request.POST.get('stock_producto')
        carrito.save()
    
    return render(request, 'app/Usuario_Iniciado.html', datos)
    

def perrito_ini(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.stock = request.POST.get('stock_producto')
        carrito.save()
    return render(request, 'app/perrito_iniciado.html', datos)  

def gato_ini(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    return render(request, 'app/gato_iniciado.html', datos)

def pajaros_ini(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    
    return render(request, 'app/pajaros_iniciado.html', datos)


@login_required
def Historial(request):
    historial = Historial_Items.objects.all()

    datos = {
            'listahistorial' : historial
            }

    return render(request, 'app/historial.html',datos)   

@login_required
def carrito(request):
    carrito = Items_Carrito.objects.all()


   
#rescato el nombre del usuario iniciado
    username1 = request.user.get_username()

#comparo el nombre de usuario iniciado con el de las suscripciones
    sucrip = Suscripcion.objects.get(username=username1)
      
#valido si esta sususcrito o no y aplico el descuento      
    if sucrip == True:
        sub_total = sum(aux.precio_producto for aux in carrito)
        descuento = round((sum(aux.precio_producto for aux in carrito)*0.05) )
        total = sum(aux.precio_producto for aux in carrito) - round((sum(aux.precio_producto for aux in carrito)*0.05) ) 

    else:   
        sub_total = sum(aux.precio_producto for aux in carrito)
        descuento = 0
        total = sum(aux.precio_producto for aux in carrito)

    datos = {
        'listaCarrito' : carrito,
        'precio' : sub_total,
        'descuento' :descuento,
        'total' :   total

        }
    if request.method == 'POST' :
        historial = Historial_Items()
        historial.nombre_producto = request.POST.get('nombre_producto')
        historial.precio_producto = request.POST.get('precio_producto')
        historial.imagen= request.POST.get('imagen_producto')
        historial.save()

    return render(request, 'app/carrito.html',datos) 


def eliminar_carrito(request, id):
    producto = Items_Carrito.objects.get(id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")

    return redirect(to= "carrito")





@login_required
def suscripcion_ini(request):
    UsuariosAll = Usuarios.objects.all()
    datos = {
        'listaUsuarios' : UsuariosAll
    }
    if request.method == 'POST' :
        suscripcion = Suscripcion()
        suscripcion.username = request.POST.get('username')
        suscripcion.suscrito = request.POST.get('suscrito')
        suscripcion.save() 

    return render(request, 'app/Suscripcion_iniciado.html', datos)




@login_required
def todo_ini(request):
    response = requests.get('https://digimon-api.herokuapp.com/api/digimon').json()
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll,
        'listajson' : response }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.stock = request.POST.get('stock_producto')
        carrito.save()
    
    return render(request, 'app/todos_iniciado.html', datos)  




@login_required
def ayuda_ini(request):
    return render(request, 'app/paginaAyuda_iniciado.html')   
    
      

def cuenta(request):
    return render(request, 'app/cuenta.html')



def pago(request):
    return render(request, 'app/pago.html')   

def iniciar_sesion(request):
    return render(request, 'app/iniciar_sesion.html')   

def seguimiento(request):
    return render(request, 'app/Seguimiento.html')    

def seguimiento2(request):
    return render(request, 'app/seguimiento2.html')

def codigo2(request):
    return render(request, 'app/codigo2.html')

def desuscripcion(request):
    return render(request, 'app/desuscripcion.html')

@permission_required('app.add_producto')
def agregar_p(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
    return render(request, 'app/agregar_producto.html', datos)    

@permission_required('app.change_producto')
def modificar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto Modificado correctamente!')
            datos['form'] = formulario

    return render(request, 'app/modificar_producto.html', datos)    

@login_required
def listar_producto(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request, 'app/listar_producto.html', datos)  
    
@permission_required('app.delete_producto')
def eliminar_producto(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_producto")



def registro(request):
    datos = {
        'form' : RegistroUsuarioForm() }
        
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            groups = Group.objects.get(name="cliente")
            user.groups.add(groups)
            usuario = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            messages.success(request,'usuario guardado correctamente!')
    return render(request, 'registration/registro.html', datos)




    