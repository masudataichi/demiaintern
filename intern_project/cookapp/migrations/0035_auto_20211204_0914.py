# Generated by Django 3.2.9 on 2021-12-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0034_alter_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
