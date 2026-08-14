# API de Gestión de Biblioteca

Este proyecto consiste en una REST API para la gestión integral de un catálogo de libros, usuarios y préstamos.

## Características Principales

- **API REST desarrollada utilizando Django REST Framework.**
- **Base de datos PostgreSQL**, alojado en Render.
- **Autenticación de usuarios con JWT** (SimpleJWT).
- **Control de acceso** según el rol del usuario (Administrador / Usuario).
- **Contraseñas protegidas** con el sistema de hashing nativo de Django (PBKDF2).
- **Validación de la información recibida mediante Serializers** .
- **Actualización y validación automática del estado** (`status`) al registrar o devolver un préstamo.
- **Filtros** por categoría, estado de disponibilidad y coincidencia textual.
- **Documentación con Swagger UI**.
- **Despliegue** en Render Web Service integrado con GitHub.

---

## Tecnologías y Librerías Utilizadas

- Python 3.12
- Django 6.1
- Django REST Framework 3.15
- djangorestframework-simplejwt
- drf-spectacular (Swagger UI / OpenAPI 3.0)
- django-cors-headers
- psycopg2-binary
- gunicorn
- python-dotenv
- PostgreSQL (en producción) / SQLite (desarrollo local)

---

## Estructura del Proyecto

```text
Biblioteca-API/
│
├── apps/
│   ├── books/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── loans/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── users/
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
│
├── biblioteca_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env
├── .gitignore
├── build.sh
├── manage.py
├── README.md
└── requirements.txt
```
---

## Roles del Sistema

El acceso a las funcionalidades del sistema depende del rol asignado a cada usuario.

| ID Rol / Tipo | Descripción |
| :---: | :--- |
| **Administrador** | Acceso total al panel `/admin/`, creación y gestión completa de libros y usuarios del sistema. |
| **Público General** | Registro, autenticación, consulta del catálogo disponible y solicitud de sus propios préstamos. |

## Lógica de Negocio Implementada

### Creación de Préstamos
Al registrar un préstamo:
- Se valida que el libro exista en la base de datos.
- Se verifica que el estado del libro sea `AVAILABLE` (Disponible).
- Se crea el registro del préstamo asignado al usuario autenticado.
- Se actualiza automáticamente el estado del libro a `BORROWED` (Prestado).

### Devolución y Cancelación
Al devolver o cancelar un préstamo:
- Se actualiza el registro del préstamo como completado/devuelto.
- Se restaura automáticamente el estado del libro a `AVAILABLE` (Disponible).
- Se mantiene la trazabilidad histórica de la operación en la base de datos.

---

## Instalación y Configuración Local

### 1️⃣ Clonar el repositorio
```bash
git clone [https://github.com/Havilag/Biblioteca-API.git](https://github.com/Havilag/Biblioteca-API.git)
cd Biblioteca-API

python -m venv venv
.\venv\Scripts\activate

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

SECRET_KEY=tu_clave_secreta_django
DEBUG=True
ALLOWED_HOSTS=localhost
DB_NAME=biblioteca_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```
---

## Documentación Swagger

Una vez iniciada la aplicación, la documentación interactiva estará disponible en:
`http://localhost:8000/api/docs/swagger/`

Y la versión desplegada en producción en:
[https://biblioteca-api-bcjz.onrender.com/api/docs/swagger/](https://biblioteca-api-bcjz.onrender.com/api/docs/swagger/)

Desde Swagger podrás:
- Consultar los endpoints disponibles.
- Autenticarte ingresando tu token JWT en el botón **Authorize**.
- Probar las peticiones (`GET`, `POST`, `PUT`, `DELETE`).
- Ver los parámetros de entrada y esquemas de datos.
- Revisar las respuestas de cada endpoint.

## Autor

**Hector Avila Gonzales**

Proyecto desarrollado como práctica de Backend con:
- Django & Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger UI
- Render Deployment