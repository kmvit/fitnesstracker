from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    GENDER=(
        ('men', 'Мужчина'),
        ('women', 'Женщина'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    name = models.CharField(max_length=20, verbose_name='Фамилия и имя')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    growth = models.IntegerField(verbose_name='Рост')
    active = models.BooleanField(default=False, verbose_name='Оплатил')
    gender = models.CharField(max_length=10, default=2, choices=GENDER, verbose_name='Пол')

    def __str__(self):
        return f'{self.name} - телефон: {self.phone}'

    class Meta:
        verbose_name = 'Профили участников'
        verbose_name_plural = 'Профиль участника'

