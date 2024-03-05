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
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products , name="products"),
    path('darkroom/', views.darkroom, name="darkroom"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    path('products/canonae1program/', views.canonae1program, name="canonae1program"),
    path('products/contaxt2/', views.contaxt2, name="contaxt2"),
    path('products/ilfordhp5/', views.ilfordhp5, name="ilfordhp5"),
    path('products/ilfordxp2/', views.ilfordxp2, name="ilfordxp2"),
    path('products/vision350d/', views.kodak50d, name="vision350d"),
    path('products/vision3250d/', views.kodak250d, name="vision3250d"),
    path('products/vision3200t/', views.kodak200t, name="vision3200t"),
    path('products/vision3500t/', views.kodak500t, name="vision3500t"),
    path('products/kodakgold200/', views.kodakgold200, name="kodakgold200"),
    path('products/mamiya7/', views.mamiya7, name="mamiya7"),
    path('products/pentax6x7/', views.pentax6x7, name="pentax6x7"),
    path('products/xpan/', views.xpan, name="xpan"),
    ]
    
