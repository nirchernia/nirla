"""
WSGI config for nirla project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ["DJANGO_SETTINGS_MODULE"] = "nirla.settings"

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nirla.settings")
#export DJANGO_SETTINGS_MODULE="nirla.settings"

application = Cling(get_wsgi_application())

