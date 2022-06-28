from django.urls import path, include
from rest_framework import routers
from . views import *
#se encarga de agregar una ruta al api
router = routers.DefaultRouter()


router.register('producto', ProductoViewSet)
router.register('Suscripcion', SuscripcionViewSet)
router.register('TipoProducto', TipoProductoViewSet)
router.register('Usuarios', UsuariosViewSet)

urlpatterns = [
     path('api/', include(router.urls)),
    
]
