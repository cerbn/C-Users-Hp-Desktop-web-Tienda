from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name="index"),
    path('perrito/',perrito,name="perrito"),
    path('gato/',gato,name="gato"),
    path('pajaros/',pajaros,name="pajaros"),
    path('todos/',todos,name="todos"),
    path('suscripcion/',suscripcion,name="suscripcion"),
    path('ayuda/',ayuda,name="ayuda"),
    path('registro/',registro,name="registro"),
    path('codigo2/',codigo2,name="codigo2"),

    path('usu_ini/', usuario_iniciado, name="usu_ini" ),
    path('perrito_ini/',perrito_ini,name="perrito_ini"),
    path('gato_ini/',gato_ini,name="gato_ini"),
    path('pajaro_ini/',pajaros_ini,name="pajaros_ini"),
    path('suscripcion_ini/',suscripcion_ini,name="suscripcion_ini"),
    path('ayuda_ini/',ayuda_ini,name="ayuda_ini"),
    path('todo_ini/',todo_ini,name='todo_ini'),
    path('carrito/', carrito, name="carrito"),
    path('cuenta/', cuenta, name="cuenta"),
    path('Historial/', Historial, name="Historial"),
    path('pago/', pago, name="pago"),
    path('seguimiento/', seguimiento, name="seguimiento"),
    path('seguimiento2/', seguimiento2, name="seguimiento2"),
    
    path('conf_pago/', conf_pago, name="conf_pago"),
   

    path('agregar_p', agregar_p, name="agregar_p"),
    path('modificar_producto/<codigo>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<codigo>/', eliminar_producto, name="eliminar_producto"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),

    
 
    path('eliminar_carrito/<id>/', eliminar_carrito, name="eliminar_carrito"),


    path('desuscripcion/', desuscripcion, name="desuscripcion"),

    path('registro/', registro, name="registro"),
    
 


]

