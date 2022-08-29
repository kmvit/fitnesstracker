# Generated by Django 3.2.14 on 2022-08-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20220827_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everydayreport',
            name='weight',
            field=models.FloatField(verbose_name='Вес утром'),
        ),
        migrations.AlterField(
            model_name='everyweekreport',
            name='hips',
            field=models.FloatField(verbose_name='Талия'),
        ),
        migrations.AlterField(
            model_name='everyweekreport',
            name='neck',
            field=models.FloatField(verbose_name='Шея'),
        ),
        migrations.AlterField(
            model_name='everyweekreport',
            name='waist',
            field=models.FloatField(verbose_name='Бедра'),
        ),
        migrations.AlterField(
            model_name='everyweekreport',
            name='weight',
            field=models.FloatField(verbose_name='Вес'),
        ),
    ]
