# Generated by Django 3.2.14 on 2022-09-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='growth',
            field=models.IntegerField(blank=True, verbose_name='Рост'),
        ),
    ]