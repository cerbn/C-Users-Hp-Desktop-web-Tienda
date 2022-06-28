from distutils.command.upload import upload
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo
    
    class Meta:
       db_table = 'db_tipo_producto'
'''
class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo
    
    class Meta:
       db_table = 'db_tipo_producto'
'''

class Producto(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)   
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
       db_table = 'db_producto'


class Items_Carrito(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(null=True)
    stock = models.IntegerField(null=True)
    class Meta:
        db_table = 'db_Items_Carrito'


class Historial_Items(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(null=True)
    class Meta:
        db_table = 'db_historial'






class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    #tipo =  models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)   
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    contrasenia = models.CharField(max_length=200) 


    class Meta:
       db_table = 'db_usuario'

class Suscripcion(models.Model):
    username = models.CharField(max_length=200)
    suscrito = models.BooleanField(default=True)

    class Meta:
       db_table = 'db_suscripcion'



# python manage.py makemigrations = crea el script de la bd
# python manage.py migrate

