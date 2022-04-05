from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
    

def probandoTemplate(request, nombre):

    listaNotas = [2, 3, 4, 8, 10]

    plantilla = loader.get_template('template1.html')

    return HttpResponse(plantilla.render({"name": nombre, "ahora": datetime.now(), "notas": listaNotas}))


def segundoTemplate(request, nombre):

    plantilla = loader.get_template('template2.html')

    return HttpResponse(plantilla.render({"name": nombre}))




