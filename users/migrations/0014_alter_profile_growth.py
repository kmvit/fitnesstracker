# Generated by Django 3.2.14 on 2022-09-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='growth',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рост'),
        ),
    ]
