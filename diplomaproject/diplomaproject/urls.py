"""
URL configuration for diplomaproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from polls import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products', views.products , name="products"),
    path('darkroom', views.darkroom, name="darkroom"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('contact', views.contact, name="contact"),
    path('canonae1program', views.canonae1program, name="canonae1program"),
    path('contaxt2', views.contaxt2, name="contaxt2"),
    path('ilfordhp5', views.ilfordhp5, name="ilfordhp5"),
    path('ilfordxp2', views.ilfordxp2, name="ilfordxp2"),
    path('vision350d', views.kodak50d, name="vision350d"),
    path('vision3250d', views.kodak250d, name="vision3250d"),
    path('vision3200t', views.kodak200t, name="vision3200t"),
    path('vision3500t', views.kodak500t, name="vision3500t"),
    path('kodakgold200', views.kodakgold200, name="kodakgold200"),
    path('mamiya7', views.mamiya7, name="mamiya7"),
    path('pentax6x7', views.pentax6x7, name="pentax6x7"),
    path('xpan', views.xpan, name="xpan"),
    ]
