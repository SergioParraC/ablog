from django.urls import path
from user import views

urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('login', views.LoginUserView.as_view(), name='login'),
    path('logout', views.logoutUserView, name='logout')
]
