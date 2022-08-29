from django.contrib.auth.models import User
from django.db import models
from datetime import date

from core.models import EveryWeekReport
from users.models import Profile


class Task(models.Model):
    """Задания на неделю"""
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Участник')
    date = models.DateField(default=date.today, verbose_name='Дата')
    text = models.TextField(verbose_name='Задание')

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Добавить задание'

    def __str__(self):
        return f'{self.profile} - {self.date}'


class Plank(models.Model):
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Участник')
    date = models.DateField(default=date.today, verbose_name='Дата')
    days = models.IntegerField('Дней')
    callories = models.IntegerField('Каллории')
    protein = models.IntegerField('Белок')
    steps = models.IntegerField('Шаги')

    class Meta:
        verbose_name = 'Планки'
        verbose_name_plural = 'Добавить планку'

    def __str__(self):
        return f'{self.profile} - {self.date}'