
from django.db import models

from django.forms.utils import pretty_name
from django.http import request
from django.shortcuts import redirect, render

from django.db.models.fields import EmailField

from django.forms.utils import to_current_timezone
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Submission, Threadlist, User, Thread, Friends, Threadlist, Like
from .forms import PasswordForm, SubmissionForm, FriendsForm, ThreadlistForm, SearchForm

from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.utils.crypto import get_random_string

from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import SignupForm, ThreadForm
from django.contrib.auth.decorators import login_required, user_passes_test

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EmailAuthenticationForm

# Create your views here.
def top(request):
    return render(request, 'cookapp/top.html')

class login_view(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = "cookapp/login.html"
    success_url = reverse_lazy('home')
    


def logout(request):
    return render(request,'cookapp/logout.html')





class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "cookapp/signup.html"
    success_url = reverse_lazy('signup_complete')

    def form_valid(self,form):
        user = form.save(commit = False)
        user.userID = get_random_string(15)
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self,form):
        messages.error(self.request,"失敗")
        return super().form_invalid(form)

def signup_complete(request):
    return render(request,'cookapp/signup_complete.html')

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
    user = request.user
    if request.method == 'POST':
        word = request.POST['word']
        if word == '和食':
            word = 11
        if word == '洋食':
            word = 12
        if word == '中華':
            word = 13
        if word == 'アジア':
            word = 14
        if word == 'カレー':
            word = 15
        if word == '焼肉':
            word = 16
        if word == '鍋':
            word = 17
        if word == '麺類':
            word = 18
        if word == '軽食':
            word = 19
        if word == 'スイーツ':
            word = 20
        if word == '飲食':
            word = 21
        if word == 'その他':
            word = 22
        place = Submission.objects.filter(place__icontains=word)
        print(place)
        category = Submission.objects.filter(category__icontains=word)
        params ={
            'form':SearchForm,
            'category':category,
            'place':place,
        }
    if Friends.objects.filter(Q(current_user = request.user) | Q(users = request.user)).exists():
        friendslist = Friends.objects.filter(Q(current_user = request.user) | Q(users = request.user))
        if Submission.objects.exclude(submissionconnection = user).exists():
            submission_exclude = Submission.objects.exclude(submissionconnection = user)
            params ={
                'submission_exclude':submission_exclude,
                'user':user,
                'form':SearchForm,
                'friendslist': friendslist,
            }
            return render(request, 'cookapp/friends.html',params)       
        if Like.objects.filter(user = user).exists():
            like = Like.objects.filter(user = user)
            submission_exclude = Submission.objects.exclude(submissionconnection = user)
            params ={
                'submission_exclude':submission_exclude,
                'user':user,
                'like':like,
                'form':SearchForm,
            }
            return render(request, 'cookapp/friends.html',params)
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
        return redirect('home')

    return render(request, 'cookapp/submission.html', params)

def friends_content(request,id):
    content = Submission.objects.get(id = id)
    content.time = content.time + 1
    content.save()
    threadlist = Thread.objects.filter(threadconnection_image = content)
    if request.method == 'POST':
        if 'comment' in request.POST:
            form = ThreadForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.threadconnection_image = content
                form.threadconnection_user = request.user
                form.save()
        if 'like' in request.POST:
            user = request.user
            if Like.objects.filter(user=user,submission=content).exists():
                like= Like.objects.get(user=user,submission=content)
                like.delete()
            else:
                Like.objects.create(user=user,submission = content)
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
        'time': content.time,
    }
    return render(request, 'cookapp/friends_contents.html',params)

def my_content(request, id):
    content = Submission.objects.get(id = id)
    thread = Thread.objects.filter(threadconnection_image = content)
    threadlist = Threadlist.objects.all()
    form1 = ThreadlistForm()
    if request.method == 'POST':
        if 'thread1' in request.POST:
            print(request.POST)
            form = ThreadForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.threadconnection_image = content
                form.threadconnection_user = request.user
                form.save()
        elif 'th' in request.POST:
                print(type(request.POST['th']))
                number = int(request.POST['th'])
                print(type(number))
                form2 = ThreadlistForm(request.POST)
                if form2.is_valid():
                    form2 = form2.save(commit=False)
                    form2.threadlistconnection_thread = thread[number]
                    form2.threadlistconnection_user = request.user
                    form2.save()
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
        'thread': thread,
        'form1': form1,
        'threadlist': threadlist,
    }
    return render(request, 'cookapp/my_content.html', params)

def friends_list(request):
    if Friends.objects.filter(Q(current_user = request.user) | Q(users = request.user)).exists():
        friendslist = Friends.objects.filter(Q(current_user = request.user) | Q(users = request.user))
        user = request.user
        number = len(friendslist)
    # friendslist = request.user.friends
        params = {
            'friendslist': friendslist,
            'user': user,         
            'number': number   
        }
        return render(request, 'cookapp/friends_list.html', params)

    return render(request, 'cookapp/friends_list.html')


def friends_profile(request,id):
    friend = User.objects.get(id = id)
    content = Submission.objects.filter(submissionconnection = friend,public_private = 11)
    if content.exists():
        randomcontent = content.order_by('?')[0]
        print(randomcontent)
        content = content.exclude(id = randomcontent.id).order_by('date')
        params = {
            'user': friend,
            'content': content,
            'randomcontent': randomcontent,
            }
    else:
        params = {
            'user':friend,
            }

    return render(request, 'cookapp/friends_profile.html',params)

def setting(request):
    user = request.user
    params = {
        'user':user,
    }
    return render(request, 'cookapp/setting.html',params)

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'cookapp/user_update.html'
    fields = ['username','email','icon']
    success_url = reverse_lazy('setting_complete')

def user_delete(request):
    return render(request,'cookapp/user_delete.html')

class UserDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'cookapp/user_delete.html'
    success_url = reverse_lazy('top')
    model = User

class MyContentDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'cookapp/my_content_delete.html'
    success_url = reverse_lazy('home')
    model = Submission

class PasswordView(LoginRequiredMixin,PasswordChangeView):
    success_url = 'setting'
    template_name = 'cookapp/password_change.html'
    form_class = PasswordForm

def friends_add_before(request):
    myuserID = request.user.userID
    params = {
        'myuserID': myuserID,
        'form': FriendsForm(),

    }
    if request.method == 'POST':
        form = FriendsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if User.objects.filter(userID = form.userID).exists():
                print(form)
                userID = form.userID
                return redirect('friends_add_after', userID)
            else:
                return render(request, 'cookapp/friends_add_before.html', params)
        else:
            params['form'] = form
            return render(request, 'cookapp/friends_add_before.html', params)
    return render(request, 'cookapp/friends_add_before.html', params)

class ContentUpdateView(LoginRequiredMixin,UpdateView):
    model = Submission
    template_name = 'cookapp/my_content_update.html'
    form_class = SubmissionForm

    success_url = reverse_lazy('home')

    def form_valid(self,form):

        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"投稿の更新に失敗しました。")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['content'] = Submission.objects.filter(submissionconnection=user)
        return context


def my_content_delete(request):
    return render(request, 'cookapp/my_content_delete.html')


@login_required
def friends_add_after(request, userID):
    from_user = request.user
    to_user = User.objects.get(userID = userID)
    myuserID = request.user.userID
    
    params = {
        'myuserID': myuserID,
        'friends': to_user,
    }
    
    if request.method == 'POST':
        print('OK')
        friends, created = Friends.objects.get_or_create(
            current_user = from_user,
            users = to_user,
        )
        friends, created = Friends.objects.get_or_create(
            current_user = to_user,
            users = from_user,
        )

        return redirect('home')

    return render(request, 'cookapp/friends_add_after.html', params)

def setting_complete(request):
    return render(request, 'cookapp/setting_complete.html')


