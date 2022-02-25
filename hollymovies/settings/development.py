from decouple import config

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['*']
