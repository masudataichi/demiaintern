from django.db import models
from django.contrib.auth.models import AbstractUser

from intern_project.cookapp.views import friends

class User(AbstractUser):
    #アイコン画像
    icon = models.ImageField(blank=True, null=True)


class Submission(AbstractUser):
    submissionconnection = models.Foreignkey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True),
    category = models. CharField(max_length=50),
    public_private = models.CharField(max_length=3),
    date = models.DateTimeField(blank=True, null=True),
    place = models.CharField(max_length=50),
    comment = models.CharField(max_length=2000)
# Create your models here.
