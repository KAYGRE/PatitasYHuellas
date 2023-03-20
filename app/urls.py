from django.urls import path
from .views import (home,nosotros,galeria,pokedex,formulario,clientes,eliminar,
                    crear,modificar,mascotas,eliminacota,crearcota,modificacota)


urlpatterns=[
    path('', home, name='home'),
    path('nosotros/', nosotros, name='nosotros'),
    path('galeria/', galeria, name='galeria'),
    path('pokedex/', pokedex, name='pokedex'),
    path('formulario/', formulario, name='formulario'),
    path('clientes/', clientes, name="clientes"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('crear/',crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('mascotas/', mascotas, name="mascotas"),
    path('eliminacota/<id1>', eliminacota, name="eliminacota"),
    path('crearcota/',crearcota, name="crearcota"),
    path('modificacota/<id1>', modificacota, name="modificacota"),
]