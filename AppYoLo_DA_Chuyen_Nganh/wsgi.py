"""
WSGI config for AppYoLo_DA_Chuyen_Nganh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppYoLo_DA_Chuyen_Nganh.settings')

application = get_wsgi_application()

app = application
