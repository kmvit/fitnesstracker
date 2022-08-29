from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        password1 = forms.CharField(label='Enter password',
                                    widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirm password',
                                    widget=forms.PasswordInput)
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'growth']





