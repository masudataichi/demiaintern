
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid


class User(AbstractUser):
    #アイコン画像
    icon = models.ImageField(blank=True, null=True)
    username_validator = UnicodeUsernameValidator()
    userID = models.CharField(max_length = 15, null = True, blank = True)

    username = models.CharField(
        verbose_name='名前(20文字まで)',
        max_length=20,
        unique=False,
        validators=[username_validator],
        error_messages={
            'unique':("A user with that username already exists."),
        },
        
    )

    email = models.EmailField(max_length=254, null=True, unique=True , verbose_name='メールアドレス') #追記　エガワ　verbose_name
  



class Submission(models.Model):
    #外部キー
    submissionconnection = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissionconnection')
    #画像
    image = models.ImageField(upload_to='media', blank=True, null=True)
  
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
    category = models.IntegerField(choices=CATEGORY, null=True)
    PUBLIC_PRIVATE = (
        (11, '公開'),
        (12, '非公開'),
    )
    #公開/非公開
    public_private = models.IntegerField(choices=PUBLIC_PRIVATE, null=True)
    #日付時間
    date = models.DateField(blank=True, null=True)
    #場所
    place = models.CharField(max_length=50, null=True)
    #コメント
    comment = models.CharField(max_length=2000, null=True)
    time = models.IntegerField(default=0)

class Thread(models.Model):
    threadconnection_image = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='threadconnection_image', null=True)
    threadconnection_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threadconnection_user', null=True)
    thread = models.CharField(max_length=150, null=True)
    
class Threadlist(models.Model):
    threadlistconnection_thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='threadlistconnection', null=True)
    threadlistconnection_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threadlistconnection', null=True)
    threadlist = models.CharField(max_length=150, null=True)

class Friends(models.Model):

    users = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE, null=True)#友達
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)#自分


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user', null=True)
    submission = models.ForeignKey(Submission,on_delete=models.CASCADE,related_name='submission', null=True)


