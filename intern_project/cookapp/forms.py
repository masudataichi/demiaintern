
from django import forms
from django.db.models import fields
from .models import Friends, Submission, Thread
from django.forms import ImageField

from django.contrib.auth.forms import UserCreationForm
from .models import User


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['image','category','public_private','date','place','comment']
        
        #追記（臼杵）
        widgets = {
            'comment': forms.Textarea(attrs={'rows':16, 'cols':15}),
        }



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','icon']

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread']

        widgets = {
            'thread':forms.Textarea(attrs={'rows':2, 'cols':45 }),
        }

class FriendsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userID']




