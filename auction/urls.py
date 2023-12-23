from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home-page"),
    path("signup/", signup, name="signup-page"),
    path("login/", login_page, name="login-page"),
    path("logout/", logout_page, name="logout-page"),
]
