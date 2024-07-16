from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, ProfileView, UserListView, toggle_activity

app_name = UsersConfig.name

urlpatterns = [
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('toggle_activity/<int:pk>/', toggle_activity, name='toggle_activity'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('profile/', ProfileView.as_view(), name='profile')
]
