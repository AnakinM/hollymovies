from decouple import config

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['sdadjangoapp1.herokuapp.com']
