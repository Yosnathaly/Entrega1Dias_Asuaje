from django.db import models

class Conocenos(models.Model):
    inicio= models.CharField(max_length=30)

class Productos(models.Model):

    nombre= models.CharField(max_length=40)
    tamaño= models.IntegerField()
    valor= models.IntegerField()

class Contactanos(models.Model):
    telefono= models.CharField(max_length=30)
    dirección= models.CharField(max_length=30)
