
from django.db import models
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Submission
from .forms import SubmissionForm
from django.views.generic import CreateView
from django.contrib import messages


from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import SignupForm

# Create your views here.
def top(request):
    params = {
        'login':'login',
        'signup':'signup'
    }
    return render(request, 'cookapp/top.html', params)

class login_view(LoginView):
    authentication_form = AuthenticationForm
    template_name = "cookapp/login.html"

def logout(request):
    return render(request, 'cookapp/logout.html')

class signup_view(CreateView):
    form_class = SignupForm
    template_name = "cookapp/signup.html"
    success_url = reverse_lazy('signup_complete')

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

def signup_complete(request):
    return render(request, 'cookapp/signup_complete.html')

def home(request):
    user = request.user
    params = {
        'user': user 
    }
    return render(request, 'cookapp/home.html')

def friends(request):
    return render(request, 'cookapp/friends.html')

class SubmissionView(CreateView):
    model = Submission
    template_name = 'cookapp/submission.html'
    form_class = SubmissionForm
    success_url = reverse_lazy('cookapp:home')
    def form_valid(self, form):
        submmision = form.save(commit=False)
        submmision.submissionconnection = self.request.user
        submmision.save()
        messages.success(self.request, '投稿完了しました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, '投稿失敗しました。')
        return super().form_invalid(form)



def friends_content(request):
    return render(request, 'cookapp/friends_content.html')

def my_content(request):
    return render(request, 'cookapp/my_content.html')

def friends_list(request):
    return render(request, 'cookapp/friends_list.html')

def friends_profile(request):
    return render(request, 'cookapp/friends_profile.html')

def setting(request):
    return render(request, 'cookapp/setting.html')

def friends_add_before(request):
    return render(request, 'cookapp/friends_add_before.html')

def my_content_update(request):
    return render(request, 'cookappp/my_content_update.html')

def my_content_delete(request):
    return render(request, 'cookapp/mycontent_delete.html')

def friends_add_after(request):
    return render(request, 'cookapp/friends_add_after.html')

