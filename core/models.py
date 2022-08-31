from math import log

from ckeditor.fields import RichTextField
from django.db import models
from users.forms import User
from datetime import date


class EveryDayReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Участник')
    date = models.DateField(default=date.today, verbose_name='Дата отчета')
    weight = models.FloatField(verbose_name='Вес утром')
    steps = models.IntegerField(verbose_name='Шаги')
    critical_days = models.BooleanField(default=False, verbose_name='Критические дни')
    link = models.CharField(max_length=250, default='ссылка', blank=True, verbose_name='Ссылка на отчет')
    file = models.FileField(upload_to='user_file', blank=True, verbose_name='Файл отчета')

    def __str__(self):
        return f'{self.user.profile.name} | отчет от {self.date}'

    class Meta:
        verbose_name = 'Ежедневные отчеты'
        verbose_name_plural = 'Ежедневный отчет'


class EveryWeekReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Участник')
    date = models.DateField(default=date.today, verbose_name='Дата отчета')
    weight = models.FloatField(verbose_name='Вес')
    neck = models.FloatField(verbose_name='Шея')
    waist = models.FloatField(verbose_name='Бедра')
    hips = models.FloatField(verbose_name='Талия')
    side_view = models.ImageField(upload_to='user_photo', blank=True, verbose_name='Вид сбоку')
    front_view = models.ImageField(upload_to='user_photo', blank=True, verbose_name='Вид спереди')
    back_view = models.ImageField(upload_to='user_photo', blank=True, verbose_name='Вид сзади')

    def fat(self):
        if self.user.profile.gender == 'men':
            fat = 495 / (1.0324 - 0.19077 * log(self.hips - self.neck, 10) + 0.15456 * log(self.user.profile.growth, 10)) - 450
        else:
            fat = 495 / (1.29579 - 0.35004 * log(self.hips + self.waist - self.neck, 10) + 0.22100 * log(self.user.profile.growth, 10)) - 450
        return f'{fat:.{2}f}'

    def __str__(self):
        return f'{self.user.profile.name} | отчет от {self.date}'

    class Meta:
        verbose_name = 'Еженедельные отчеты'
        verbose_name_plural = 'Еженедельный отчет'
        ordering = ['-date',]


class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название страницы')
    slug = models.SlugField(unique=True, verbose_name='URL')
    text = RichTextField('Содержание', blank=True)
    image = models.ImageField(upload_to='author', blank=True, verbose_name='Изображение автора')

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title


class PageImage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница')
    image_before = models.ImageField(upload_to='reviews', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото отзыв'
        verbose_name_plural = 'Фото отзывы'


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    text = models.TextField('Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
