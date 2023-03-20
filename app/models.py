from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Tipocli(models.Model):
    idtipo = models.BigAutoField(primary_key=True, verbose_name='Id del Tipo de Cliente') 
    nomtipo = models.CharField(max_length=30, verbose_name='Nombre del Tipo de Cliente')

    def __str__(self):
        return self.nomtipo
#persona natural adopta   persona juridica colaborador

class Cliente(models.Model):
    rutcliente = models.CharField(max_length=10, primary_key=True, verbose_name='Rut del Cliente') 
    nombrecliente = models.CharField(max_length=40, verbose_name='Nombre de Cliente')
    contacto = models.IntegerField( verbose_name='Telefono de Contacto', null=True)
    tipocli = models.ForeignKey(Tipocli , on_delete=models.CASCADE)

    def __str__(self):
        return self.rutcliente 


class Tipomascota(models.Model):
    idtipo = models.BigAutoField(primary_key=True, verbose_name='Id del Tipo de Mascota') 
    nomtipo = models.CharField(max_length=30, verbose_name='Nombre del Tipo de Mascota')

    def __str__(self):
        return self.nomtipo


class Mascotas(models.Model):
    codmascota = models.IntegerField(primary_key=True, verbose_name='Codigo de Mascota') 
    nombremascota = models.CharField(max_length=30, verbose_name='Nombre de la Mascota')
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    tipomascota = models.ForeignKey(Tipomascota , on_delete=models.CASCADE)

    def __str__(self):
        return self.nombremascota
