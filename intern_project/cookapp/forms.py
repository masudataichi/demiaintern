from django import forms
from django.contrib.auth.backends import UserModel
from django.db.models import fields
from .models import Friends, Submission, Thread, Threadlist
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .models import User
from django.contrib.auth import authenticate, get_user_model
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _


class SubmissionForm(forms.ModelForm):

    image = forms.ImageField(widget=forms.FileInput) # ★追加　エガワ

    class Meta:
        model = Submission
        fields = ['image','category','public_private','date','place','comment']
        
        MONTHS = { 
            1: ' 1 ', 2: ' 2 ', 3: ' 3 ', 4: ' 4 ',
            5: ' 5 ', 6: ' 6 ', 7: ' 7 ', 8: ' 8 ',
            9: ' 9 ', 10: ' 10 ', 11: ' 11 ', 12: ' 12 '
        }

        #追記（臼杵）
        widgets = {
            'comment': forms.Textarea(attrs={'rows':7, 'cols':15}),
            'date': forms.SelectDateWidget(years=[x for x in range(1990, 2030)], months=MONTHS), #追記　エガワ
            'place': forms.TextInput(attrs={'placeholder': '場所を入力'}),

        }


class SearchForm(forms.Form):
    word = forms.CharField(max_length=100)

    widgets = {
        word:forms.TextInput(attrs={'placeholder':'カテゴリー、場所'})
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
class ThreadlistForm(forms.ModelForm):
    class Meta:
        model = Threadlist
        fields = ['threadlist']

class FriendsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userID']

        widgets = {
            'userID':forms.TextInput(attrs={'placeholder': '友達のIDを入力してください'})
        }

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

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'autoforcus':True}))
    password = forms.CharField(label=("Passeord"), strip=False, widget=forms.PasswordInput)
    error_messeges = {
        'invalid_login': "Eメールアドレス　または　パスワードに誤りがあります。",
        'inactive': _("This account is inactive."),
    }
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        # Set the label for the "email" field.
        self.email_field = UserModel._meta.get_field("email")
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messeges['invalid_login'],
                    code='invalid_login',
                    params={'email': self.email_field.verbose_name})
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(self.error_messeges['inactive'], code='inactive')

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


