# Generated by Django 3.0.4 on 2021-11-23 08:02

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0019_merge_20211119_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='名前(20文字まで)'),
        ),
    ]
