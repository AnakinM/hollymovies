from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea, NumberInput

from viewer.models import Genre


class MovieForm(Form):
    title = CharField(max_length=128)
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = DateField(widget=NumberInput(attrs={'type': 'date'}))
    description = CharField(widget=Textarea, required=False)
