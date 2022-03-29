from django.http import HttpResponse

from Postres.models import Productos

def Productos (request):
    return HttpResponse('Bienvenidos a nuestra pastelería')

def Productos(self):

      Productos = Productos(nombre="Red Velvet", tamaño="15", valor= "25")
      Productos.save()
      documentoDeTexto = f"--->Productos: {Productos.nombre}, tamaño: {Productos.tamaño}, valor: {Productos.valor}"


      return HttpResponse(documentoDeTexto)