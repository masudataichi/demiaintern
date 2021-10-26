from django.shortcuts import render

# Create your views here.
def top(request):
    params = {
        'login':'login',
        'signup':'signup'
    }
    return render(request, 'cookapp/top.html', params)

def login(request):
    return render(request, 'cookapp/login.html')

def logout(request):
    return render(request, 'cookapp/logout.html')

def signup(request):
    return render(request, 'cookapp/signup.html')

def signup_complete(request):
    return render(request, 'cookapp/signup_complete.html')

def home(request):
    return render(request, 'cookapp/home.html')

def friends(request):
    return render(request, 'cookapp/friends.html')

def submission(request):
    return render(request, 'cookapp/submission.html')

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

