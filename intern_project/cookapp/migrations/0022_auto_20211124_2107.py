# Generated by Django 3.0.4 on 2021-11-24 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0021_comment_subcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcomment',
            name='target',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='SubComment',
        ),
    ]
