@echo off
echo 🔧 Creando estructura...
mkdir backend\community_project 2>nul
mkdir backend\usuarios 2>nul
mkdir backend\reportes 2>nul
mkdir frontend\templates 2>nul
mkdir frontend\static\css 2>nul
mkdir frontend\static\js 2>nul
mkdir docs 2>nul
mkdir media 2>nul

echo Django==5.0.6 > requirements.txt
echo venv/ > .gitignore
echo # Sistema de Reportes > README.md

echo import os > backend\community_project\settings.py
echo BASE_DIR = os.path.dirname(__file__) >> backend\community_project\settings.py
echo DEBUG = True >> backend\community_project\settings.py

echo from django.contrib import admin > backend\community_project\urls.py
echo from django.urls import path >> backend\community_project\urls.py
echo urlpatterns = [path('admin/', admin.site.urls)] >> backend\community_project\urls.py

git add .
git commit -m "🏗️ Estructura base automática" 2>nul

echo ✅ Listo. Ahora haz:
echo git remote add origin https://github.com/jhoyce-z/sistema-reportes-comunidad.git
echo git push -u origin main
pause