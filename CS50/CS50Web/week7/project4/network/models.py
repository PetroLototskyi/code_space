from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils import timezone


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    text = models.TextField(default="No description available", blank=False, null=False)
    created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    def __str__(self):
        return f"Post {self.id} made by {self.user} pon {self.created.strftime("%d/%m/%Y %H:%M:%S")}"

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

    def __str__(self):
        return f"{self.follower} is following {self.following}"

class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")

    class Meta:
        unique_together = ("user", "post")

    def __str_(self):
        return f"{self.user} liked {self.post}"

