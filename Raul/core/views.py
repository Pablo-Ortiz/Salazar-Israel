from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.

@login_required
def index(request):
    data = {
        'form': FormularioCliente()
    }
    if request.method == 'POST':
        form = FormularioCliente(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list/<str:username>")
        data["form"]=form
    return render(request, 'index.html', data)

@login_required
def Form(request):
    data = {
        'form': FormularioCliente()
    }
    if request.method == 'POST':
        form = FormularioCliente(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list/<str:username>")
        data["form"]=form
    return render(request, 'registration/form.html', data)

@login_required
def profile(request, username):
    current_user = request.user
    cliente = Automovil.cliente.username
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        list = Automovil.objects.get(cliente=username)
    elif cliente == username:
        list = Automovil.objects.all()
    else:
        user = current_user
        list = cliente
    return render(request, 'registration/profile.html', {'user': user, 'list': list})

@login_required
def List(request, username):
    current_user = request.user
    cliente = Automovil.cliente
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        list = Automovil.objects.all()
    elif cliente == username:
        list = Automovil.objects.get(cliente=username)
    else:
        user = current_user
        list = Automovil.objects.all()
    return render(request, 'registration_data/list.html', {'user': user,'list': list})