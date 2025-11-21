from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista_reportes, name='lista_reportes'),
    path('crear/', views.crear_reporte, name='crear_reporte'),
    path('editar/<int:pk>/', views.editar_reporte, name='editar_reporte'),
    path('eliminar/<int:pk>/', views.eliminar_reporte, name='eliminar_reporte'),
]