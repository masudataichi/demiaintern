from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.top, name='top'),
    path('login/', views.login_view.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('signup_complete',views.signup_complete,name='signup_complete'),
    path('home', views.home, name='home'),
    path('friends', views.friends, name='friends'),
    path('submission', views.SubmissionView, name='submission'),
    path('friends_content/<int:id>', views.friends_content, name='friends_content'),
    path('my_content/<int:id>', views.my_content, name='my_content'),
    path('friends_list', views.friends_list, name='friends_list'),
    path('friends_profile/<int:id>', views.friends_profile, name='friends_profile'),
    path('setting', views.setting, name='setting'),
    path('friends_add_before', views.friends_add_before, name='friends_add_before'),
    path('my_content_update', views.ContentUpdateView.as_view(), name='my_content_update'),
    path('my_content_delete/<int:pk>', views.MyContentDeleteView.as_view(), name='my_content_delete'),
    path('friends_add_after/<str:userID>', views.friends_add_after, name="friends_add_after"), 
    path('user_update/<int:pk>',views.UserUpdateView.as_view(),name='user_update'),
    path('logout2',LogoutView.as_view(),name='logout2'),
    path('user_delete/<int:pk>',views.UserDeleteView.as_view(),name='user_delete'),
    path('password_change',views.PasswordView.as_view(),name='password_change'),
    path('setting_complete',views.setting_complete,name='setting_complete'),
]