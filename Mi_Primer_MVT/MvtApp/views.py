from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from MvtApp.models import Papa, Mama, Hermano

# Create your views here.

def inicio(request):

    plantilla = loader.get_template('inicio.html')

    return HttpResponse(plantilla.render())


def papa(request, nombre, edad, fecha_nac,):

    papa = Papa(nombre=nombre, edad=edad, fecha_nac=fecha_nac)
    papa.save()

    plantilla = loader.get_template('papa.html')

    return HttpResponse(plantilla.render({"name": nombre, "age": edad, "date": fecha_nac}))


def mama(request, nombre, edad, fecha_nac, idioma):

    mama = Mama(nombre=nombre, edad=edad, fecha_nac=fecha_nac, idioma=idioma)
    mama.save()

    plantilla = loader.get_template('mama.html')

    return HttpResponse(plantilla.render({"name": nombre, "age": edad, "date": fecha_nac, "language": idioma}))


def hermano(request, nombre, edad, fecha_nac,):

    hermano = Hermano(nombre=nombre, edad=edad, fecha_nac=fecha_nac)
    hermano.save()

    plantilla = loader.get_template('hermano.html')

    return HttpResponse(plantilla.render({"name": nombre, "age": edad, "date": fecha_nac}))