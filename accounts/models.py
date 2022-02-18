from django.contrib.auth.models import User
from django.db.models import CASCADE, Model, OneToOneField, TextField, IntegerField, CharField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    gender = CharField(max_length=6, blank=True)
    biography = TextField(blank=True)
