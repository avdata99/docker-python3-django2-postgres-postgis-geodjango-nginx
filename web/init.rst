Inicializar GeoDjango
=====================

Todo esto solo se requiere una vez (en este repo ya esta hecho y listo).
Crear el proyecto Django:

.. code:: bash

  django-admin startproject mydjango

Agregar directorios para *media* y *static*.

.. code:: bash 

  mkdir mydjango/static 
  mkdir mydjango/media

 
Además agregar *django.contrib.gis* a **INSTALLED_APPS**.

Migrar, estáticos y superuser

.. code:: bash

  python manage.py migrate
  python manage.py collectstatic
  python manage.py createsuperuser


Crear una app de prueba

.. code:: bash

  python manage.py startapp geoapp


