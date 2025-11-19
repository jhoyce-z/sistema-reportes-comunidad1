# 📢 Sistema de Reportes Comunitarios

> Proyecto desarrollado por un **equipo de 7 integrantes** bajo metodología **Scrum** en sprints intensivos de 3 días.  
> Permite a los ciudadanos reportar problemas comunitarios (basura, baches, alumbrado, seguridad) con autenticación segura y seguimiento de estado.

🔗 **Demo (desarrollo)**: `http://localhost:8000`  
📌 **Tablero Scrum (Trello)**: [Enlace al tablero](https://trello.com/b/...) *(reemplazar con tu enlace real)*

---

## 🧑‍🤝‍🧑 Equipo y Roles (Scrum)

| Rol | Integrante | Responsabilidades clave |
|-----|-------------|--------------------------|
| **Scrum Master** | Fidel | Coordina reuniones diarias, resuelve bloqueos, garantiza flujo Scrum. |
| **Product Owner** | Jeyson | Define historias de usuario, prioriza backlog, valida entregas. |
| **Backend Developer** | Samir | Modelos Django, lógica de negocio, API. |
| **Backend Developer** | Angel | Autenticación, seguridad, vistas funcionales. |
| **Backend Developer** | Junior | Integración, pruebas, preparación de CRUD. |
| **Frontend Developer** | Miguel | Templates HTML/CSS/Bootstrap, UX responsive. |
| **Full Stack / DevOps** | Juan | Configuración de repositorio, entorno, base de datos y despliegue inicial. |

> 🔄 **Rotación prevista**: En Sprint 2, los roles se reevaluarán para equilibrar aprendizajes.

---

## 🚀 Objetivo del Sprint #1 (3 días)

> **“Sistema funcional de reportes comunitarios con autenticación y CRUD básico”**  
> Entrega mínima viable (MVP):
> - ✅ Registro y login de usuarios (US1, US2)
> - ✅ Creación de reportes con ubicación y categoría (US3)
> - ✅ Lista, edición y eliminación de *mis reportes* (US4, US5)

---

## 🛠️ Tecnologías Utilizadas

| Capa | Tecnología |
|------|------------|
| **Framework Backend** | Django 5.0 |
| **Base de Datos** | MySQL 8.0 |
| **Frontend** | HTML5 + Bootstrap 5 + CSS |
| **Autenticación** | Django Auth + `UserCreationForm` |
| **Gestión de Código** | Git + GitHub |
| **Gestión Ágil** | Trello (tablero Scrum) |
| **IDE** | Visual Studio Code |
| **Entorno** | `venv` + Python 3.10+ |

---

## 📋 Requisitos para Ejecutar Localmente

### 🔧 Instalación

```bash
# 1. Clonar repositorio
git clone https://github.com/jhoyce-z/sistema-reportes-comunidad.git
cd sistema-reportes-comunidad

# 2. Crear y activar entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar base de datos MySQL
#    - Crear base de datos: CREATE DATABASE reportes_comunidad;
#    - Editar credenciales en: backend/community_project/settings.py → DATABASES

# 5. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 6. (Opcional) Crear superusuario
python manage.py createsuperuser

# 7. Ejecutar servidor
python manage.py runserver
