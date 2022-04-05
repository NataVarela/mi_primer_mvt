from django.db import models

# Create your models here.

class Papa(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nac = models.DateField()


class Mama(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
    idioma = models.CharField(max_length=40)


class Hermano(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nac = models.DateField()