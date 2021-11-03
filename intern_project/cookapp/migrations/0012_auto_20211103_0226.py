# Generated by Django 3.0.4 on 2021-11-02 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0011_auto_20211103_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='friends',
        ),
        migrations.AddField(
            model_name='friends',
            name='from_user',
            field=models.ManyToManyField(related_name='from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friends',
            name='to_user',
            field=models.ManyToManyField(related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Friends_Request',
        ),
    ]