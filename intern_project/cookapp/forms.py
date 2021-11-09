from django import forms
from django.db.models import fields
from .models import Friends, Submission, Thread
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .models import User


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['image','category','public_private','date','place','comment']



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','icon']

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread']

class FriendsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userID']

class PasswordForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=("新しいパスワード"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=("新しいパスワード　（確認）"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )




