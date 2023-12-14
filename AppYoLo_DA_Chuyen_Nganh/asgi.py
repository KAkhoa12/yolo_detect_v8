"""
ASGI config for AppYoLo_DA_Chuyen_Nganh project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppYoLo_DA_Chuyen_Nganh.settings')

application = get_asgi_application()
