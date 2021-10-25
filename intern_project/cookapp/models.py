from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #アイコン画像
    icon = models.ImageField(blank=True, null=True)

# Create your models here.
