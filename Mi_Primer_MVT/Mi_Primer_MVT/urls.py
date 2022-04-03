"""Mi_Primer_MVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import calcular_fecha, probandoTemplate, saluda, saluda2, saluda_con_nombre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', saluda),
    path('saludar2/', saluda2),
    path('saluda-nombre/<nombre>/<edad>', saluda_con_nombre),
    path('calcular-fecha/<nombre>/<edad>', calcular_fecha),
    path('probandoTemplate/', probandoTemplate),
]
