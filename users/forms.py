from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from users.models import Profile

User = get_user_model()


class CreationForm(UserCreationForm):
        model = User
        username = UsernameField(
            label='Логин (на латинице)',
            widget=forms.TextInput(attrs={'autofocus': True})
        )
        password1 = forms.CharField(label='Пароль',
                                    widget=forms.PasswordInput)
        password2 = forms.CharField(label='Подтвердите пароль',
                                    widget=forms.PasswordInput)
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'growth', 'age']





