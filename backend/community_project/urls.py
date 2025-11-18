from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def inicio_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"<h1>¡Hola, {request.user.username}!</h1><p>Estás en el sistema de reportes.</p>")
    return HttpResponse("<h1>Bienvenido</h1><p>Por favor, <a href='/login/'>inicia sesión</a> o <a href='/registro/'>regístrate</a>.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
]