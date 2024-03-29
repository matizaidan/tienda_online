#!/bin/bash
# Permisos de ejecucion: chmod +x setup.sh
# Crear entorno virtual
python3 -m venv myvenv

# Activar entorno virtual
source myvenv/bin/activate

# Instalar Django
pip install django

# Crear nuevo proyecto de Django
django-admin startproject mysite .

# Configurar proyecto
sed -i "s/TIME_ZONE = 'UTC'/TIME_ZONE = 'America/Argentina/Cordoba'/" mysite/settings.py
sed -i "s/LANGUAGE_CODE = 'en-us'/LANGUAGE_CODE = 'es-ar'/" mysite/settings.py
echo "STATIC_ROOT = BASE_DIR / 'static'" >> mysite/settings.py
sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']/" mysite/settings.py

# Aplicar migraciones
python manage.py migrate

# Iniciar servidor web
python manage.py runserver
