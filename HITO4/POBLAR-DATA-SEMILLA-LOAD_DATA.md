
# LOAD-DATA (manage.py)

## Paso a paso para poblar la data a dicho proyecto

1. Haber realizado los MODELS
2. Haber realizado las MIGRATE 
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Crear los .json necesarios
4. Ejecutar los comandos LOAD-DATA para cada .json segín el ORDEN correspondiente

Ejemplo:
```bash
python manage.py loaddata m7_python/data/users.json

python manage.py loaddata m7_python/data/regiones_comunas.json

python manage.py loaddata m7_python/data/inmuebles.json
```

```
COMANDO loaddata dentro del manage -> la APP nuestra m7_python y la carpeta data y el nameArchivo.json
python manage.py loaddata m7_python/data/users.json
```

- Limpiar data de las tablas de nuestra db
```bash
python manage.py flush
```
---
# DATA SEMILLA
## Etapas de como crear nuestro `.JSON` para migrar (poblar) 
0. Conectarnos a nuestro Entorno Virtual
1. Crear Model
```py
rom django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

```
2. Hacer MIGRACIONES
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Crear en nuestra app (ejemplo de mi app de nombre `web`) la carpeta `data`
```
myproject
web --|
     data
      |---|
         post.json
```

4. Armar nuestro/s `.json`
```json
[
    {
        "model": "web.post",
        "pk": 1,
        "fields": {
            "title": "Cocinar",
            "text": "ensaladas de la semana",
        }
    },
    {
        "model": "web.post",
        "pk": 2,
        "fields": {
            "title": "Hacer caminata",
            "text": "Incrementar 1 kilómetro por semana",
        }
    },
    {
        "model": "web.post",
        "pk": 3,
        "fields": {
            "title": "Descansar",
            "text": "periodos breves de 45 minutos",
        }
    }
]
```
5. Ejecutar el comando `LOAD-DATA` que nos brinda DJANGO en nuestro manage.py
```bash
python manage.py loaddata web/data/post.json
```

**IMPORTANTE: debemos cargar a priori (en principio) aquellos datos (tablas) que no requieren de una relación `FK`**

**IMPORTANTE - La compatibilidad de los CAMPOS (FIELDS) en relación a nuestros MODELS y los JSON creados**

**IMPORTANTE - El orden para cargar (POBLAR) la data a nuestra DB (según las RELACIONES)**