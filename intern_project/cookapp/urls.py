from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('login/', views.login_view.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup', views.signup_view.as_view(), name='signup'),
    path('signup_complete', views.signup_complete, name='signup_complete'),
    path('home', views.home, name='home'),
    path('friends', views.friends, name='friends'),
    path('submission', views.SubmissionView.as_view(), name='submission'),
    path('friends_content', views.friends_content, name='friends_content'),
    path('my_contents', views.my_content, name='my_content'),
    path('friends_list', views.friends_list, name='friends_list'),
    path('friends_profile', views.friends_profile, name='friends_profile'),
    path('setting', views.setting, name='setting'),
    path('friends_add_before', views.friends_add_before, name='friends_add_before'),
    path('my_content_update', views.my_content_update, name='my_content_update'),
    path('my_content_delete', views.my_content_delete, name='my_content_delete'),
    path('friends_add_after', views.friends_add_after, name="friends_add_after"),    
]