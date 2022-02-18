from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea, ModelForm, ChoiceField

from accounts.models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        profile = Profile(biography=None, gender=None, user=result)
        if commit:
            profile.save()
        return result


class UserProfileUpdateForm(ModelForm):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    class Meta:
        model = Profile
        fields = '__all__'

    gender = ChoiceField(choices=GENDER_CHOICES, required=False)
    biography = CharField(
        label='Tell us your story with movies', widget=Textarea, required=False
    )
