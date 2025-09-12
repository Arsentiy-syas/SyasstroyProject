from django.urls import path
from django.urls import reverse_lazy, re_path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('listusers/', views.ListUsers.as_view(), name='listuserss'),
]