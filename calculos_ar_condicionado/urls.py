from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_ambiente, name='criar_ambiente'),
    path('listar-ambientes/', views.lista, name='listar'),
    path('editar/<int:ambiente_id>/', views.editar, name='editar'),
]
