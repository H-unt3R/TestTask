"""
WSGI config for task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#path = '/home/KamiBarut/munichliving'
path = '/home/Hunt33R/hunt33r.pythonanywhere.com/task/settings.py'

if path not in sys.path:
    sys.path.insert(0, path)
    #sys.path.append('/home/KamiBarut/munichliving')
    #sys.path.append(path)
    #sys.path.append("/home/KamiBarut/munichliving")
os.environ['DJANGO_SETTINGS_MODULE'] = 'task.settings.py'
#os.environ['DJANGO_SETTINGS_MODULE'] = 'munichliving.settings'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'munichliving.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#import os
#import sys
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'munichliving.settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "munichliving.settings")
