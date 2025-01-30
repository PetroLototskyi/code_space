from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from decimal import Decimal
from django.contrib import messages

from .models import User, Auction_listing, Bid, Comment, Category


def index(request):

    #  listings = Auction_listing.objects.all()
     active_listings=Auction_listing.objects.filter(is_active=True)
     all_categories = Category.objects.all()


     return render(request, "auctions/index.html", {
        "listings": active_listings,
        "categories" : all_categories
    })

def selected_category(request):
     if request.method == "POST":
        category_string= request.POST['category']
        all_categories = Category.objects.all()

        if category_string =="All":
            active_listings=Auction_listing.objects.filter(is_active=True)
            # category = "All"
            return render(request, "auctions/index.html", {
                "listings": active_listings,
                "categories" : all_categories
             })

        else:
            category = Category.objects.get(category_Name=category_string)
            # print(type(category))
            active_listings=Auction_listing.objects.filter(is_active=True, category=category)

        return render(request, "auctions/index.html", {
            "listings": active_listings,
            "categories" : all_categories,
            "selected_category": category

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


def new_listing(request):
    if request.method == 'GET':
        all_categories = Category.objects.all()
        return render(request, "auctions/new_listing.html", {
            "categories" : all_categories
        })

    if request.method == 'POST':
        base_price = request.POST['base_price']
        name = request.POST['name']
        description = request.POST['description']
        image = request.POST['image_link']
        is_active = True
        created = datetime.now()
        # dd/mm/YY H:M:S
        # dt_string = created.strftime("%d/%m/%Y %H:%M:%S")
        # print("date and time =", dt_string)
        current_price = base_price
        current_user=request.user

        category = request.POST['category']
        # print (request.POST)
        category_options=Category.objects.get(category_Name=category)

        # Create a new Auction_listing object and save it to the database
        auction_listing = Auction_listing(
        base_price=base_price,
        name=name,
        description=description,
        image=image,
        is_active=is_active,
        created=created,
        current_price=current_price,
        category=category_options,
        owner=current_user
        )
        # Save the auction listing to the database
        auction_listing.save()

        listings = Auction_listing.objects.all()

        #  This one shown all listing active and not active
        #     return render(request, "auctions/index.html", {
        #     "listings": listings
        # })

        # Redirect to Index page
        return HttpResponseRedirect(reverse(index))


def item(request, id):
    item_obj=Auction_listing.objects.get(pk=id)
    in_watchlist = request.user in item_obj.watchlist.all()
    all_comments=Comment.objects.filter(auction=item_obj)
    lister = request.user == item_obj.owner
    highest_bid_amount, highest_bid_user = item_obj.get_highest_bid()
    # print(highest_bid_amount)
    # print(highest_bid_user)
    return render(request, "auctions/item.html", {
        "item": item_obj,
        "in_watchlist": in_watchlist,
        "all_comments": all_comments,
        "lister": lister,
        "highest_bid_amount": highest_bid_amount,
        "highest_bid_user": highest_bid_user
    })

def won_auction(request):
    if request.method == 'GET':
        non_active_listings=Auction_listing.objects.filter(is_active=False)
        user= request.user
        won_list=[]
        for item in non_active_listings:
            if item.get_highest_bid()[1] == user:
                won_list.append(item)
        if len(won_list)==0:
            messages.info(request, f"You have not won any auctions.") # message

        return render(request, "auctions/won.html", {
            "won_list": won_list
        })

def remove_watch(request, id):
    item_obj=Auction_listing.objects.get(pk=id)
    item_obj.watchlist.remove(request.user)
    return HttpResponseRedirect(reverse("item", args=(id, )))


def add_watch(request, id):
    item_obj=Auction_listing.objects.get(pk=id)
    item_obj.watchlist.add(request.user)
    return HttpResponseRedirect(reverse("item", args=(id, )))

def watchlist(request):
    items = request.user.item_watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "items": items
    })

def add_comment(request, id):
    if request.method == "POST":
        user = request.user
        item_obj = Auction_listing.objects.get(pk=id)
        comment_text = request.POST['new_comment']

        # Create a new comment object
        new_comment = Comment(
            user=user,
            auction=item_obj,
            comment=comment_text
        )

        # Save the comment to the database
        new_comment.save()

        # Redirect to the item page
        return HttpResponseRedirect(reverse("item", args=(id,)))

def add_bid(request, id):
    if request.method == "POST":
        user = request.user
        item_obj = Auction_listing.objects.get(pk=id)
        bid_value=request.POST['new_bid']
        # convert to Decimal
        bid_amount = Decimal(bid_value)
        #Retriving the price of listing
        current_price=item_obj.current_price
        # print(type(bid_amount))
        # print(type(current_price))

        if not Bid.objects.filter(auction=item_obj).exists() and bid_amount >= current_price:
                new_bid = Bid (
                    user=user,
                    auction=item_obj,
                    bid_amount=bid_amount
                )

                new_bid.save()
                item_obj.current_price = bid_amount
                item_obj.save()

                messages.success(request, f"The Bid of $'{bid_amount}' succsesfuly placed") # message

        elif Bid.objects.filter(auction=item_obj).exists() and bid_amount > current_price:

                new_bid = Bid (
                    user=user,
                    auction=item_obj,
                    bid_amount=bid_amount
                )
                new_bid.save()
                item_obj.current_price = bid_amount
                item_obj.save()
                messages.success(request, f"The Bid of $'{bid_amount}' succsesfuly placed") # message

        else:
            messages.success(request, f"Bid must be equal to or greater than the starting price, or higher than the current bid.") # message

        return HttpResponseRedirect(reverse("item", args=(id,)))

def close_auction(request, id):
   if request.method =='POST':
        item_obj=Auction_listing.objects.get(pk=id)
        item_obj.is_active =False
        item_obj.save()
        messages.info(request, "Auction has been successfully closed.")
        return HttpResponseRedirect(reverse("item", args=(id,)))
