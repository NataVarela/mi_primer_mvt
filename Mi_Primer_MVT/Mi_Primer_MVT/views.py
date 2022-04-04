from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader

def saluda(request):

    return HttpResponse('Hola Mundo!')


def saluda2(request):

    return HttpResponse('Hola desde mi segundo template')


def saluda_con_nombre(request, nombre, edad):

    return HttpResponse(f'Hola {nombre} tenes {edad} años!')


def calcular_fecha(request, nombre, edad):

    año_nacimiento = 2022 - int(edad)

    return HttpResponse(f'Hola {nombre} naciste en {año_nacimiento}!')


def probandoTemplate(request, nombre):

    listaNotas = [2, 3, 4, 8, 10]

#    miHtml = open('C:/Users/ezequ/Desktop/Natu/1. Programación/1. Curso CoderHouse/mi_primer_mvt/Mi_Primer_MVT/Mi_Primer_MVT/templates/template1.html')

#    plantilla = Template(miHtml.read())

#    miHtml.close()

#    miContexto = Context({"name": nombre, "ahora": datetime.now(), "notas": listaNotas})

#    return HttpResponse(plantilla.render(miContexto))

    plantilla = loader.get_template('template1.html')

    return HttpResponse(plantilla.render({"name": nombre, "ahora": datetime.now(), "notas": listaNotas}))


def segundoTemplate(request, nombre):

    plantilla = loader.get_template('template2.html')

    return HttpResponse(plantilla.render({"name": nombre}))




