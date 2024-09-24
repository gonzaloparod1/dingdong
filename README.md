# DINGDONG

DINGDONG es una aplicación web de arriendos de inmuebles creada con Python y Django.

### Tecnologías

- Python 3
- Django 5

### Descripción

DINGDONG es una plataforma para arrendar inmuebles. Existen dos tipos de usuarios

### Características

- Registro e inicio de sesión de usuarios
- Navegación de inmuebles disponibles
- Editar Perfil
- Editar Inmueble
- Filtros de busqueda

### Instalación y Configuración

#### Requisitos Previos

- Python 3.x
- Pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

#### Pasos de Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd onlyflans
   ```

2. Crea y activa un entorno virtual:

   ```bash
   virtualenv venv
   source venv/Scripts/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env` (opcional):

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

7. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

### Uso

1. Abre tu navegador web y navega a `http://localhost:8000/` para ver la página de inicio.
2. Usa el panel de administración en `http://localhost:8000/admin/` para gestionar el contenido de la aplicación.

### Rutas

- "/data"
- "/migrations"
- "/templates"
- "/static"
- "/management
- "/registration

### Integrantes

- Gonzalo Parodi 
  - [GitHub](<https://github.com/gonzaloparod1>)

### Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva característica (`git checkout -b feature/nueva-caracteristica`).
3. Haz commit de tus cambios (`git commit -am 'Añadida nueva característica'`).
4. Empuja tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

### Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de [gonzalo.parodi@gmail.com].
