# Generated by Django 3.2.14 on 2022-08-18 17:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_everydayreport_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Задание')),
                ('week_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.everyweekreport', verbose_name='Еженедельный отчет')),
            ],
            options={
                'verbose_name': 'Задания',
                'verbose_name_plural': 'Добавить задание',
            },
        ),
        migrations.CreateModel(
            name='Plank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('days', models.IntegerField(verbose_name='Дней')),
                ('callories', models.IntegerField(verbose_name='Каллории')),
                ('protein', models.IntegerField(verbose_name='Белок')),
                ('steps', models.IntegerField(verbose_name='Шаги')),
                ('week_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.everyweekreport', verbose_name='Еженедельный отчет')),
            ],
            options={
                'verbose_name': 'Планки',
                'verbose_name_plural': 'Добавить планку',
            },
        ),
    ]
