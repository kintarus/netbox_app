from django.urls import path
from .views import BaseView, LoginView, RegisterView, LogoutUser

urlpatterns = [
    path('index', BaseView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('', LogoutUser, name='logout_user'),
]