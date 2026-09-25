from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='home'),
    path('juego/<int:pk>/', views.game_detail, name='game_detail'),
    path('juego/nuevo/', views.game_create, name='game_create'),
    path('juego/<int:pk>/editar/', views.game_update, name='game_update'),
    path('juego/<int:pk>/eliminar/', views.game_delete, name='game_delete'),
]
