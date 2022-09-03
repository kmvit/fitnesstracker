from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER=(
        ('men', 'Мужчина'),
        ('women', 'Женщина'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь (латиницей)')
    name = models.CharField(max_length=100, verbose_name='Фамилия и имя')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    growth = models.IntegerField(blank=True, default='', null=True, verbose_name='Рост')
    age = models.IntegerField(blank=True, null=True, verbose_name='Возраст')
    active = models.BooleanField(default=False, verbose_name='Оплатил')
    gender = models.CharField(max_length=10, default=2, choices=GENDER, verbose_name='Пол')

    def __str__(self):
        return f'{self.name} - телефон: {self.phone}'

    class Meta:
        verbose_name = 'Профили участников'
        verbose_name_plural = 'Профиль участника'


@receiver(post_save, sender=User)
def create_favorites(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

