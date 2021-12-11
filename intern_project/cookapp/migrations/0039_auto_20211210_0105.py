# Generated by Django 3.2 on 2021-12-09 16:05

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0038_merge_20211209_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, default='ジバニャン.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='ユーザーネーム'),
        ),
    ]