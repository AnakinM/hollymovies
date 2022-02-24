from decouple import config
import django_heroku

django_heroku.settings(locals())
SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['sdadjangoapp1.herokuapp.com']
