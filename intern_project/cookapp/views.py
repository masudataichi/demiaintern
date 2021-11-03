
from django.db import models
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Submission, User, Thread
from .forms import SubmissionForm
from django.views.generic import CreateView
from django.contrib import messages
from django.utils.crypto import get_random_string


from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import SignupForm, ThreadForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def top(request):
    return render(request, 'cookapp/top.html')

class login_view(LoginView):
    authentication_form = AuthenticationForm
    template_name = "cookapp/login.html"

def logout(request):
    return render(request, 'cookapp/logout.html')

class signup_view(CreateView):
    model = User
    form_class = SignupForm
    template_name = "cookapp/signup.html"
    success_url = reverse_lazy('signup_complete')

    def form_valid(self,form):
        user = form.save(commit = False)
        user.userID = get_random_string(15)
        user.user = self.request.user
        user.save()
        messages.success(self.request,"完了")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"失敗")
        return super().form_invalid(form)


def signup_complete(request):
    return render(request, 'cookapp/signup_complete.html')
@login_required
def home(request):
    user = request.user
    content = Submission.objects.filter(submissionconnection=user)
    if content.exists():
        randomcontent = content.order_by('?')[0]
        content = content.exclude(id = randomcontent.id)
        params = {
            'user': user,
            'content': content,
            'randomcontent': randomcontent,
            }
    else:
        params = {
            'user': user,
            }

    return render(request, 'cookapp/home.html', params)

def friends(request):
    return render(request, 'cookapp/friends.html')

def SubmissionView(request):
    params = {
        'form': SubmissionForm(),
    }
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submissionconnection = request.user
            submission.save()
        else:
            params['form'] = form
            return render(request, 'cookapp/submission.html', params)

    return render(request, 'cookapp/submission.html', params)

def friends_content(request):
    return render(request, 'cookapp/friends_content.html')

def my_content(request, id):
    content = Submission.objects.get(id = id)
    threadlist = Thread.objects.filter(threadconnection_image = content)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.threadconnection_image = content
            form.threadconnection_user = request.user
            form.save()
    if content.category == 11:
        content.category = '和食'
    if content.category == 12:
        content.category = '洋食'
    if content.category == 13:
        content.category = '中華'
    if content.category == 14:
        content.category = 'アジア'
    if content.category == 15:
        content.category = 'カレー'
    if content.category == 16:
        content.category = '焼肉'
    if content.category == 17:
        content.category = '鍋'
    if content.category == 18:
        content.category = '麺類'
    if content.category == 19:
        content.category = '軽食'
    if content.category == 20:
        content.category = 'スイーツ'
    if content.category == 21:
        content.category = '飲食'
    if content.category == 22:
        content.category = 'その他'
    if content.public_private == 11:
        content.public_private = '公開'
    if content.public_private == 12:
        content.public_private = '非公開'
    params = {
        'content': content,
        'form': ThreadForm(),
        'threadlist': threadlist,
    }
    return render(request, 'cookapp/my_content.html', params)

def friends_list(request):
    return render(request, 'cookapp/friends_list.html')

def friends_profile(request):
    return render(request, 'cookapp/friends_profile.html')

def setting(request):
    return render(request, 'cookapp/setting.html')

def friends_add_before(request):
    return render(request, 'cookapp/friends_add_before.html')

def my_content_update(request):
    return render(request, 'cookapp/my_content_update.html')

def my_content_delete(request):
    return render(request, 'cookapp/my_content_delete.html')

def friends_add_after(request):
    return render(request, 'cookapp/friends_add_after.html')

