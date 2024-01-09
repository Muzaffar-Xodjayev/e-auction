from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home-page"),
    path("signup/", signup, name="signup-page"),
    path("create_listing/", create_listing, name="create-listing-page"),
    path("category/", category, name="category-page"),
    path("category/<int:pk>/", category_page, name="category-sort-page"),
    path("watchlist_page/", watchlist_page, name="watch-list-page"),
    path("delete_watchlist_page/<int:pk>/", delete_watching_list, name="delete-watching-list"),
    path("listing_detail/<int:pk>/", listing_detail, name="listing-detail-page"),
    path("comment/<int:pk>/", comment, name="comment-page"),
    path("edit_listing/<int:pk>/", edit_listing, name="edit-listing-page"),
    # path("watchlist/", watch_list, name="watchlist-page"),
    path("login/", login_page, name="login-page"),
    path("logout/", logout_page, name="logout-page"),
]
