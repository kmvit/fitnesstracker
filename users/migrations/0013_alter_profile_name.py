# Generated by Django 3.2.14 on 2022-09-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20220902_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Фамилия и имя'),
        ),
    ]
