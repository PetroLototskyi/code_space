from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Post, Follow, Like
from django.shortcuts import render, get_object_or_404

from .models import User


# View to display all posts
def index(request):
    posts = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "network/index.html", {
        "posts": posts
    })

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Ensure the user is the one who created the post
    if request.user != post.user:
        return redirect("index")

    if request.method == "POST":
        content = request.POST.get("content")

        # Update the post content
        post.content = content
        post.save()

        # Redirect back to the post page or wherever you want
        return redirect("index")

    return render(request, "network/index.html", {
        "post": post
    })

@login_required
def profile(request, username):
    # Get the user by username
    user = get_object_or_404(User, username=username)

    # Ensure a user cannot follow themselves
    if request.user == user:
        return render(request, "network/profile.html", {
            "user": user,
            "posts": [],
            "message": "You cannot follow yourself."
        })

    # Get the posts of the user
    posts = Post.objects.filter(user=user).order_by('-timestamp')


    # Check if the current user is following the profile's user
    is_following = Follow.objects.filter(follower=request.user, following=user).exists()

    # Handle follow/unfollow
    if request.method == "POST":
        if is_following:
            # Unfollow the user
            Follow.objects.filter(follower=request.user, following=user).delete()
        else:
            # Follow the user
            Follow.objects.create(follower=request.user, following=user)

        # Redirect back to the profile page after the action
        return HttpResponseRedirect(reverse("profile", args=[username]))

    # Count the number of followers and following
    followers_count = user.followers.count()
    following_count = user.following.count()

    return render(request, "network/profile.html", {
        "user": user,
        "posts": posts,
        "followers_count": followers_count,
        "following_count": following_count,
        "is_following": is_following
    })

# View to create a new post
@login_required
def new_post(request):
    if request.method == "POST":
        content = request.POST["content"]
        post = Post(user=request.user, content=content)
        post.save()
        return redirect("index")
    return render(request, "network/new_post.html")

# View to like/unlike a post
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

# View to follow/unfollow a user
@login_required
def toggle_follow(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    if user_to_follow == request.user:
        return JsonResponse({"error": "You cannot follow yourself."}, status=400)

    follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    if not created:
        follow.delete()
        followed = False
    else:
        followed = True

    return JsonResponse({"followed": followed})



# View to display all posts from users that the current user follows
@login_required
def following(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(user__in=[f.following for f in followed_users]).order_by('-timestamp')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "network/following.html", {
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
