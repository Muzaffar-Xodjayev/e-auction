from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import *


# Create your views here.


def home(request):
    listings = Listing.objects.filter(is_publish=True)
    if listings:
        context = {"data": listings}
    else:
        context = {"status": "There is no information"}
    return render(request, "home.html", context)


@login_required
def listing_detail(request, pk):
    context = {}
    listing = Listing.objects.get(id=pk)
    if request.POST:
        bid = request.POST["bid"]
        if int(bid) > listing.price:
            b = Bid.objects.create(listing_id=listing, author=request.user, bid=bid)
            b.save()
            listing.price = bid
            listing.save()
            context["status"] = "Your BID have been put successfully"
            context['col'] = 'alert-success'
        else:
            context["status"] = "BID should be greater than listing's current price."
            context['col'] = 'alert-danger'
    if not WatchList.objects.filter(listing_id=listing).exists():
        w = WatchList.objects.create(listing_id=listing, user=request.user)
        w.save()
    comments = Comment.objects.filter(listing_id=listing)
    bids = Bid.objects.filter(listing_id=listing)
    context['data'] = listing
    context["comments"] = comments
    context["bids"] = bids
    return render(request, "listing_detail.html", context)


@login_required
def comment(request, pk):
    if request.POST:
        listing = Listing.objects.get(id=pk)
        comment_message = request.POST["comment_message"]
        c = Comment.objects.create(listing_id=listing, author=request.user, message=comment_message)
        c.save()
        messages.success(request, "Your comment have been published successfully")
        return redirect(f"/listing_detail/{listing.id}")


@login_required
def create_listing(request):
    context = {}
    data = Category.objects.all()
    context["data"] = data
    if request.POST:
        title = request.POST["title"]
        img = request.POST["image"]
        cat = request.POST["category"]
        category = Category.objects.get(name=cat)
        desc = request.POST["description"]
        price = request.POST["price"]
        listing = Listing.objects.create(author=request.user, title=title, category=category, img=img, description=desc,
                                         price=price)
        listing.save()
        context["status"] = "Listing have been successfully created."
        context["col"] = "alert-success"

    return render(request, "create_listing.html", context)


def category(request):
    context = {}
    data = Category.objects.all()
    context["data"] = data
    return render(request, "category.html", context)


def category_page(request, pk):
    context = {}
    data = Category.objects.get(id=pk)
    listing = Listing.objects.filter(category=data)
    context["listing"] = listing
    return render(request, "category.html", context)


@login_required
def watchlist_page(request):
    context = {}
    data = WatchList.objects.filter(user=request.user)
    context["data"] = data
    return render(request, "watchlist_page.html", context)


@login_required
def delete_watching_list(request, pk):
    data = WatchList.objects.filter(listing_id=pk).delete()
    return redirect("watch-list-page")


def signup(request):
    context = {}
    if request.POST:
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            return redirect("home-page")
        else:
            context['status'] = 'This username already exists !!!'
            context['col'] = 'alert-danger'
    return render(request, "register.html", context)


def login_page(request):
    context = {}
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home-page")
        else:
            context['status'] = 'Username or Password incorrect !!!'
            context['col'] = 'alert-danger'
    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect("home-page")
