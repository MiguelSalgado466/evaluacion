from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("tienda/", views.lista_tienda, name="tienda"),
]