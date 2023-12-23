from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home-page"),
    path("signup/", signup, name="signup-page"),
    path("listing_detail/<int:pk>/", listing_detail, name="listing-detail-page"),
    path("comment/<int:pk>/", comment, name="comment-page"),
    path("watchlist/", watch_list, name="watchlist-page"),
    path("login/", login_page, name="login-page"),
    path("logout/", logout_page, name="logout-page"),
]
