from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea, NumberInput, ModelForm

from viewer.models import Genre, Movie


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")


def dupa_validator(value):
    if "dupa" in value.lower():
        raise ValidationError("Value contains restricted word.")


def unique_words_validator(value):
    word_list = value.strip('.').split(' ')
    if len(set(word_list)) != len(word_list):
        raise ValidationError("Description does not contain unique words.")


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("Only past dates are allowed here.")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

    title = CharField(max_length=128, validators=[capitalized_validator])
    released = PastMonthField(widget=NumberInput(attrs={'type': 'date'}))
    description = CharField(widget=Textarea, required=False, validators=[dupa_validator, unique_words_validator])

    def clean(self):
        result = super().clean()
        if result['genre'].name == "Comedy" and result['rating'] > 6:
            self.add_error("genre", f"Can't be Comedy if rated {result['rating']}")
            self.add_error("rating", f"Can't be rated {result['rating']} if genre is Comedy")
            raise ValidationError("Comedies aren't so good to ba rated over 6")
        return result


class GenreForm(Form):
    name = CharField(max_length=40)
