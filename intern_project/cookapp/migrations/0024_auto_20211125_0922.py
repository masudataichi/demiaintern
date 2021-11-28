# Generated by Django 3.0.4 on 2021-11-25 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0023_merge_20211124_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='threadlist',
            old_name='threadlistconnection',
            new_name='threadlistconnection_thread',
        ),
        migrations.AddField(
            model_name='threadlist',
            name='threadlistconnection_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threadlistconnection', to=settings.AUTH_USER_MODEL),
        ),
    ]