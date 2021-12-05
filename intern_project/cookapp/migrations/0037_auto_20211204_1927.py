# Generated by Django 3.0.4 on 2021-12-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0036_merge_20211204_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
