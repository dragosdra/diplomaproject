from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from polls.models import User

def home(request):
    return render(request, "index.html")


def products(request):
    return render(request, 'products.html')



def darkroom(request):
    return render(request, 'darkroom.html')


def login(request):
    if request.method == 'POST':
        user = authenticate(username= request.POST.get('username'), password= request.POST.get('password'))
        print(user)
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        print(request.POST)
        User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password'))
    return render(request, 'register.html')


def contact(request):
    return render(request, 'contact.html')

def canonae1program(request):
    return render(request, 'canonae1program.html')


def contaxt2(request):
    return render(request, 'contaxt2.html')


def ilfordhp5(request):
    return render(request, 'ilfordhp5.html')


def ilfordxp2(request):
    return render(request, 'ilfordxp2.html')


def kodak50d(request):
    return render(request, 'kodak50d.html')


def kodak250d(request):
    return render(request, 'kodak250d.html')


def kodak250d(request):
    return render(request, 'kodak250d.html')


def kodak200t(request):
    return render(request, 'kodak200t.html')

def kodak500t(request):
    return render(request, 'kodak500t.html')

def kodakgold200(request):
    return render(request, 'kodakgold200.html')

def mamiya7(request):
    return render(request, 'mamiya7.html')

def pentax6x7(request):
    return render(request, 'pentax6x7.html')

def xpan(request):
    return render(request, 'xpan.html')


# Create your views here.
