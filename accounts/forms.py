from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True):
        self.instance.is_active = True
        result = super().save(commit)
        profile = Profile(biography=None, gender=None, user=result)
        if commit:
            profile.save()
        return result
