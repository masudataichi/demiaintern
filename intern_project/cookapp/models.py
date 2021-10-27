from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related




class User(AbstractUser):
    #アイコン画像
    #変更しました、コンフリクト対策
    icon = models.ImageField(blank=True, null=True)
  


class Submission(models.Model):
    submissionconnection = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissionconnection')
    image = models.ImageField(blank=True, null=True)
    CATEGORY = (
        (11, '和食'),
        (12, '洋食'),
        (13, '中華'),
        (14, 'アジア'),
        (15, 'カレー'),
        (16, '焼肉'),
        (17, '鍋'),
        (18, '麺類'),
        (19, '軽食'),
        (20, 'スイーツ'),
        (21, '飲食'),
        (22, 'その他'),
    )
    category = models. IntegerField(max_length=50, choices=CATEGORY)
    PUBLIC_PRIVATE = (
        (11, '公開'),
        (12, '非公開'),
    )
    public_private = models.IntegerField(max_length=3, choices=PUBLIC_PRIVATE)
    date = models.DateTimeField(blank=True, null=True)
    place = models.CharField(max_length=50)
    comment = models.CharField(max_length=2000)

# Create your models here.

