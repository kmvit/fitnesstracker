# Generated by Django 3.2.14 on 2022-09-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='growth',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рост'),
        ),
    ]
