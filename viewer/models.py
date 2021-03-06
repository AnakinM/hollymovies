from PIL import Image
from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, \
    DateTimeField, ImageField


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Movie(Model):
    title = CharField(max_length=128)
    image = ImageField(default="default_movie.jpg", upload_to="movies_thumbnails")
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Movie, self).save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.title}; {self.released.year}"
