# Generated by Django 3.2.14 on 2022-09-02 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_age'),
        ('core', '0017_alter_everyweekreport_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everyweekreport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Участник'),
        ),
    ]
