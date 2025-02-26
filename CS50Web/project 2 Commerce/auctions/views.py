from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 
from .models import User, Listing, Bids, Comment, Watchlist
from .forms import NewListing, NewBids



def index(request):
    return render(request, "auctions/index.html", {
        "Listings": Listing.objects.filter(status=True),
        "active": True
    })

def closed(request):
    return render(request, "auctions/index.html", {
        "Listings": Listing.objects.filter(status=False),
        "active": False
    })
@login_required
def watchlist(request):
    watchlist_items = Watchlist.objects.filter(user=request.user)
    listings = Listing.objects.filter(id__in=watchlist_items.values('listing_id'))
    return render(request, "auctions/watchlist.html", {
        "Listings": listings
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create(request):
    if request.method =="POST":
        form = NewListing(request.POST)
        if form.is_valid():
            #create a from but not save into the data base by settin commit=False
            post = form.save(commit=False)
            post.poster = request.user
            post.save()
        else:
            #if the inputs are not valid the page render with the invalid input so can the user adjust on them 
            return render(request, "auctions/create.html", {
            "form" : form
            })
        return redirect("index")
    else:
        #if the user doent submmit a from the page render new one 
        form = NewListing()
    return render(request, "auctions/create.html", {'form':form})

def listing(request, id):
    listing_data = Listing.objects.get(id=id)
    comments = Comment.objects.filter(commented_on=listing_data)
    if request.user.is_authenticated:
        watchlist_item = Watchlist.objects.filter(user=request.user, listing=id).exists()
        is_the_poster = request.user == listing_data.poster
        is_the_winner = request.user == listing_data.winner
        bid_form = NewBids(listing=listing_data)
    else:
        watchlist_item = None
        bid_form = None
        is_the_poster = False
        is_the_winner = False
    
    context = {
        "listing": listing_data,
        "watchlist_item":watchlist_item,
        "is_the_poster": is_the_poster,
        "is_the_winner":is_the_winner,
        "bid_form":bid_form,
        "comments": comments,
        "bid_number": listing_data.number_of_bids
    }
    
    return render(request, "auctions/listing.html", context)

def categories(request):
    return render(request, "auctions/categories.html")


def category(request, name):
    categories_dict = {v: k for k, v in Listing.categories_list}
    listings = Listing.objects.filter(category=categories_dict.get(name))
    return render(request, "auctions/category.html", {
        "listings": listings,
        "name": name
    })

@login_required
def add_remove_watchlist(request, id):
    watchlist_items = Watchlist.objects.filter(user=request.user, listing=id)
    
    if watchlist_items.exists():
       watchlist_items.delete()
    else:
        listing_item = Listing.objects.get(id=id)
        Watchlist.objects.create(user=request.user, listing=listing_item)
    
    return redirect("listing", id=id)

@login_required
def place_bid(request, id):
    listing_item = Listing.objects.get(id=id)
    if listing_item.status:
        if request.method == "POST":
            form = NewBids(request.POST, listing=listing_item)
            if form.is_valid():
                bid = form.save(commit=False)
                bid.bider = request.user
                bid.bid_on = listing_item
                bid.save()
                listing_item.current_bid = bid.bid_value
                listing_item.number_of_bids += 1
                listing_item.save()
                return redirect("listing", id=id)
            else:
                return render(request, "auctions/listing.html", {
                    "listing": listing_item,
                    "bid_form": form,
                })
    return redirect("listing", id=id)

@login_required 
def close_bid(request, id):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "close_bid":
            listing_item = Listing.objects.get(id=id)
            highest_bid = Bids.objects.filter(bid_on=listing_item).order_by('bid_value').first()
            if highest_bid:
                listing_item.winner = highest_bid.bider
                listing_item.status = 'False'
                listing_item.save()
                messages.success(request, "You have successfully closed this listing.")
            return redirect("listing", id=id)

@login_required
def add_comment(request, id):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add_comment":
            listing_item = Listing.objects.get(id=id)
            comment_text = request.POST.get("comment")
            Comment.objects.create(commentor=request.user, commented_on=listing_item, comment=comment_text)
    return redirect("listing", id=id)
    
    
