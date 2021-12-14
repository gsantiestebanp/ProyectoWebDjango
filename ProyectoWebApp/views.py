from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'ProyectoWebApp/home.html')

def tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html')


