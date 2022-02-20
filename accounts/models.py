from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, CharField, TextField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    gender = CharField(max_length=6, blank=True)
    biography = TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
