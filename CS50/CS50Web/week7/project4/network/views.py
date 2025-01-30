from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
import json

from .models import User, Post, Follow, Like

PAGES_DISPLAYED = 10

@login_required
def edit(request, post_id):

    if request.method == "POST":
        data = json.loads(request.body)
        edit_post= Post.objects.get (pk=post_id)
        edit_post.text = data["text"]
        edit_post.save()
        return JsonResponse({"status": "success"})


def index(request):
    all_posts=Post.objects.all().order_by("-created")

    #Pagination
    paginator = Paginator (all_posts, PAGES_DISPLAYED)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "network/index.html",{
        "all_posts": all_posts,
        "posts": posts

    })


@login_required
def toggle_like(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({"likes": post.likes.count(), "liked": liked})


@login_required
def new_post(request):
    if request.method == "POST":
        text = request.POST.get("content", "").strip()
        if not text:
            return render(request, "network/new_post.html", {
                "message": "Content cannot be empty."
            })
        post = Post(user=request.user, text=text)
        post.save()
        return redirect("index")
    return render(request, "network/new_post.html")


@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(user=user).order_by("-created")  # Only get posts for this user

    # Check if the current user is following the profile user
    isFollowing = Follow.objects.filter(follower=request.user, following=user).exists()

    # Pagination
    paginator = Paginator(posts, PAGES_DISPLAYED)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "network/profile.html", {
        "posts": posts,
        "username": user.username,
        "following": Follow.objects.filter(follower=user).count(),
        "followers": Follow.objects.filter(following=user).count(),
        "isFollowing": isFollowing,
        "user_profile": user
    })


@login_required
def follow(request):
    userfollow_id = request.POST['userfollow']
    userfollow_data = User.objects.get(pk=userfollow_id)  # User to follow
    Follow.objects.create(follower=request.user, following=userfollow_data)  # Create follow relationship

    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': userfollow_data.id}))

@login_required
def unfollow(request):
    userfollow_id = request.POST['userfollow']
    userfollow_data = User.objects.get(pk=userfollow_id)  # User to unfollow
    Follow.objects.filter(follower=request.user, following=userfollow_data).delete()  # Remove follow relationship

    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': userfollow_data.id}))

@login_required
def following(request):
    current_user=User.objects.get(pk=request.user.id)
    following_people=Follow.objects.filter(follower=current_user).values_list('following', flat=True)
    following_posts = Post.objects.filter(user__in=following_people).order_by('-id')

    #Pagination
    paginator = Paginator (following_posts, PAGES_DISPLAYED)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "network/following.html",{
        "posts": posts
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
