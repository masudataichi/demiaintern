from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
from django.contrib.auth.validators import UnicodeUsernameValidator



class User(AbstractUser):
    #アイコン画像
    icon = models.ImageField(blank=True, null=True)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name='名前(20文字まで)',
        max_length=20,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique':("A user with that username already exists."),
        },
    )
  


class Submission(models.Model):
    #外部キー
    submissionconnection = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissionconnection')
    #画像
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
    #カテゴリー
    category = models. IntegerField(max_length=50, choices=CATEGORY)
    PUBLIC_PRIVATE = (
        (11, '公開'),
        (12, '非公開'),
    )
    #公開/非公開
    public_private = models.IntegerField(max_length=3, choices=PUBLIC_PRIVATE)
    #日付時間
    date = models.DateField(blank=True, null=True)
    #場所
    place = models.CharField(max_length=50)
    #コメント
    comment = models.CharField(max_length=2000)

# Create your models here.

