import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.heroku")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
