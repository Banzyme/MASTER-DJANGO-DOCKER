"""
WSGI config for twisted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

# if not config('DEBUG'):
#     print ( config('DEBUG') )
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twisted.production_settings")
# else:
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twisted.settings")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twisted.production_settings")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twisted.settings")

application = get_wsgi_application()
