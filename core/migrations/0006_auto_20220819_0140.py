# Generated by Django 3.2.14 on 2022-08-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_page_pageimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Страницу', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/author', verbose_name='Изображение автора'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
    ]
