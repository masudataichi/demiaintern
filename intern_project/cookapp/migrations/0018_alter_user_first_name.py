# Generated by Django 3.2 on 2021-11-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0017_merge_20211110_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
