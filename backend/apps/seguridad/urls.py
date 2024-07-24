from django.urls import path
from .views import listar_menus

urlpatterns = [
    path('menus/', listar_menus, name='listar_menus'),
]
