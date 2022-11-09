# hollymovies
A project for lectures on SDA on backend technologies subject that I teach.  
Version 1.  
The app is built with Django.

# How to run
1. Create `.env` file with the following content:
```dotenv
DJANGO_SECRET_KEY="this_is_very_secret"
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_STORAGE_BUCKET_NAME=""
GOOGLE_EMAIL_USER=""
GOOGLE_APP_PASSWORD=""
DEBUG="True"
```
2. Install requirements:  
`pip install -r requirements.txt`
3. Apply migrations with the following command:  
`python manage.py migrate`
4. Populate database with genres and movies:   
`python manage.py loaddata viewer_fixtures.json`
5. Create admin user   
`python manage.py createsuperuser`

