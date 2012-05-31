import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocon.settings.heroku")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()