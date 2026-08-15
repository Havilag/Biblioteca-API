# API de Gestión de Biblioteca

Este proyecto consiste en una API REST para la gestión de una biblioteca. La aplicación permite administrar libros, usuarios y préstamos, además de mantener un historial de los préstamos realizados.

Los usuarios pueden consultar los libros disponibles, realizar préstamos y revisar su propio historial. Por otro lado, el administrador tiene acceso a la gestión completa de los libros y préstamos, además de poder consultar el historial de todos los usuarios.

## Características principales

- API REST desarrollada con Django REST Framework.
- Base de datos PostgreSQL alojada en Render.
- Autenticación de usuarios mediante JWT utilizando SimpleJWT.
- Control de acceso según el tipo de usuario (Administrador / Usuario).
- Contraseñas protegidas mediante el sistema de hashing de Django (PBKDF2).
- Validación de los datos recibidos mediante Serializers.
- Gestión de libros mediante operaciones CRUD.
- Registro y gestión de préstamos.
- Actualización automática del estado del libro al realizar o devolver un préstamo.
- Historial de préstamos para consultar los préstamos realizados anteriormente.
- Los usuarios pueden consultar únicamente su propio historial.
- Los administradores pueden consultar el historial de todos los usuarios.
- Filtros por categoría, estado de disponibilidad y búsqueda por texto.
- Documentación de la API mediante Swagger UI.
- Despliegue en Render Web Service conectado con GitHub.

---

## Tecnologías y librerías utilizadas

- Python 3.12
- Django 6.1
- Django REST Framework 3.15
- djangorestframework-simplejwt
- drf-spectacular (Swagger UI / OpenAPI 3.0)
- django-cors-headers
- psycopg2-binary
- gunicorn
- python-dotenv
- PostgreSQL (producción)
- SQLite (desarrollo local)

---

## Estructura del proyecto

```text
Biblioteca-API/
│
├── books/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── history/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── loans/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
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

## Roles del sistema

El acceso a las diferentes funciones depende del tipo de usuario que haya iniciado sesión.

| Rol / Tipo | Permisos en Libros y Préstamos | Permisos en Historial |
| :---: | :--- | :--- |
| **Administrador** (`is_staff=True`) | Puede gestionar libros y préstamos, además de tener acceso al panel `/admin/`. | Puede consultar el historial de préstamos de todos los usuarios. |
| **Usuario** (`IsAuthenticated`) | Puede consultar el catálogo disponible y realizar sus propios préstamos. | Puede consultar únicamente su propio historial de préstamos. |

### Historial de préstamos

La aplicación cuenta con un módulo independiente llamado `history`, encargado de mostrar los préstamos que se han realizado.

El historial funciona de acuerdo con el usuario que realiza la consulta:

- Un usuario normal solo puede ver los préstamos asociados a su propia cuenta.
- Un administrador puede consultar los préstamos realizados por todos los usuarios.
- Los préstamos permanecen registrados después de ser devueltos.
- El historial permite consultar tanto préstamos activos como préstamos que ya fueron devueltos.

De esta forma, un usuario no puede acceder directamente a la información de préstamos de otra persona.

---

## Lógica de negocio implementada

### Creación de préstamos

Cuando un usuario solicita un libro, la API realiza varias validaciones antes de registrar el préstamo:

- Se comprueba que el libro exista.
- Se verifica que el libro se encuentre disponible (`AVAILABLE`).
- El préstamo se asigna automáticamente al usuario autenticado.
- Se registra el préstamo en la base de datos.
- El estado del libro cambia automáticamente a `BORROWED` (Prestado).

Esto evita que un mismo libro pueda ser prestado nuevamente mientras se encuentre ocupado.

### Devolución de préstamos

Cuando un libro es devuelto:

- Se actualiza el estado del préstamo.
- Se registra la devolución correspondiente.
- El estado del libro vuelve a `AVAILABLE` (Disponible).
- El préstamo continúa almacenado para poder consultarlo posteriormente desde el historial.

### Consulta del historial

El módulo `history` permite consultar los préstamos realizados anteriormente.

Para un usuario normal, la consulta se filtra utilizando el usuario autenticado, por lo que únicamente se muestran sus propios registros.

En el caso de un administrador, se permite consultar todos los registros de préstamos almacenados en el sistema.

Endpoint utilizado:

```text
/api/v1/history/
```

---

## Instalación y configuración local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Havilag/Biblioteca-API.git
cd Biblioteca-API
```

### 2. Crear el entorno virtual

En Windows:

```bash
python -m venv venv
```

Activar el entorno virtual:

```bash
.\venv\Scripts\activate
```

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Crear un archivo `.env` en la carpeta principal del proyecto.

Ejemplo:

```env
SECRET_KEY=tu_clave_secreta_django
DEBUG=True
ALLOWED_HOSTS=localhost

DB_NAME=biblioteca_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

En producción se utilizan las variables de entorno proporcionadas por Render para la conexión con PostgreSQL.

### 5. Ejecutar las migraciones

```bash
python manage.py migrate
```

### 6. Crear un usuario administrador

Para poder acceder al panel de administración:

```bash
python manage.py createsuperuser
```

El comando solicitará el nombre de usuario, correo electrónico y contraseña.

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

La API estará disponible normalmente en:

```text
http://127.0.0.1:8000/
```

---

## Documentación Swagger

La API cuenta con documentación interactiva utilizando Swagger UI mediante `drf-spectacular`.

Una vez iniciada la aplicación, se puede acceder a la documentación local desde:

```text
http://localhost:8000/api/docs/swagger/
```

También se encuentra disponible la versión desplegada en Render:

https://biblioteca-api-bcjz.onrender.com/api/docs/swagger/

Desde Swagger se pueden:

- Consultar todos los endpoints disponibles.
- Revisar los parámetros que recibe cada endpoint.
- Ver los esquemas utilizados por los Serializers.
- Autenticar usuarios mediante JWT.
- Probar las peticiones `GET`, `POST`, `PUT`, `PATCH` y `DELETE`.
- Revisar las respuestas de la API.
- Probar el endpoint de historial utilizando diferentes usuarios.

### Autenticación en Swagger

Para utilizar los endpoints que requieren autenticación:

1. Iniciar sesión mediante el endpoint correspondiente.
2. Obtener el token JWT.
3. Presionar el botón **Authorize** en Swagger.
4. Ingresar el token.
5. Ejecutar los endpoints que requieren autenticación.

Los permisos de cada endpoint se aplican según el usuario autenticado.

---

## Módulos de la API

El proyecto está dividido en cuatro aplicaciones principales.

### Books

Se encarga de la gestión de los libros.

Entre sus funciones se encuentran:

- Registrar libros.
- Consultar libros.
- Actualizar información.
- Eliminar libros.
- Filtrar por categoría.
- Consultar disponibilidad.
- Buscar libros por coincidencia de texto.

### Users

Se encarga de los usuarios y la autenticación.

Incluye:

- Registro de usuarios.
- Inicio de sesión.
- Autenticación mediante JWT.
- Control de permisos según el tipo de usuario.

### Loans

Se encarga de los préstamos.

Incluye:

- Registrar préstamos.
- Consultar préstamos.
- Actualizar préstamos.
- Registrar devoluciones.
- Validar la disponibilidad de los libros.
- Actualizar automáticamente el estado de los libros.

### History

Se encarga de consultar el historial de préstamos.

Su funcionamiento depende del usuario autenticado:

```text
Usuario
   ↓
/api/v1/history/
   ↓
Solo muestra sus propios préstamos
```

Mientras que para un administrador:

```text
Administrador
      ↓
/api/v1/history/
      ↓
Muestra el historial de todos los usuarios
```

---

## Estados utilizados

Los libros manejan diferentes estados para controlar su disponibilidad:

- `AVAILABLE`: el libro se encuentra disponible.
- `BORROWED`: el libro está actualmente prestado.
- `MAINTENANCE`: el libro no se encuentra disponible debido a mantenimiento.

Los préstamos también manejan estados para identificar si todavía están activos o si ya fueron devueltos.

---

## Base de datos

Durante el desarrollo local se puede utilizar SQLite para realizar pruebas de forma sencilla.

Para el entorno de producción se utiliza PostgreSQL, alojado en Render.

La conexión a la base de datos se configura mediante variables de entorno, evitando colocar directamente las credenciales dentro del código fuente.

---

## Despliegue

La API se encuentra desplegada en **Render Web Service** y el código fuente se mantiene en GitHub.

La aplicación utiliza PostgreSQL como base de datos en producción y Gunicorn para ejecutar el servidor.

Repositorio:

https://github.com/Havilag/Biblioteca-API

Documentación:

https://biblioteca-api-bcjz.onrender.com/api/docs/swagger/

---

## Autor

**Hector Avila Gonzales**

Proyecto desarrollado como práctica de Backend utilizando:

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger / OpenAPI
- GitHub
- Render