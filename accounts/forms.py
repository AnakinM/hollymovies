from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = CharField(
        label='Tell us your story with movies', widget=Textarea, required=False
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return result
