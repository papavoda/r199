"""
WSGI r199 for r199 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

# add path for apache
sys.path.append('/home/codenet/Django_projects/r199')
sys.path.append('/home/codenet/Django_projects/r199/r199')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'r199.settings')

application = get_wsgi_application()