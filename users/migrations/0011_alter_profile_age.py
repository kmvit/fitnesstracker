# Generated by Django 3.2.14 on 2022-09-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_growth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default='0', verbose_name='Возраст'),
        ),
    ]
