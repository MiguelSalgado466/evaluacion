from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1>Bienvenido a la Tienda</h1>")


def lista_tienda(request):
    return HttpResponse("<h1>Lista de productos de la tienda</h1>")