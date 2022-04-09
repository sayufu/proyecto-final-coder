from django.urls import path
from App import views


urlpatterns = [
    path('',views.inicio, name=""),
    path('jugadores',views.jugadores, name="Jugadores"),
    path('entrendores',views.entrenadores, name="Entrenadores"),
    path('sponsors',views.sponsors, name="Sponsors"),
]