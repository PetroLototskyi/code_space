from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class Category(models.Model):
    category_Name=models.CharField(max_length = 64)

    def __str__(self):
        return self.category_Name

class Auction_listing(models.Model):
    base_price = models.DecimalField(max_digits=7, decimal_places=2)
    name = models.CharField(max_length=64)
    description = models.TextField(default="No description available")
    image = models.TextField(default="")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now())
    current_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null = True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="item_watchlist")

    def __str__(self):
        return f"\n {self.name}: {self.is_active} \n category: {self.category} \n starting price ${self.current_price} \n created: {self.created.strftime("%d/%m/%Y %H:%M:%S")} \n"

    def get_highest_bid(self):
        highest_bid = self.auction_bid.order_by('-bid_amount').first()
        if highest_bid:
            return highest_bid.bid_amount, highest_bid.user
        return None, None  # No bids placed



class Bid(models.Model):
    bid_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    auction = models.ForeignKey(Auction_listing, on_delete=models.CASCADE,blank=True, null=True, related_name="auction_bid")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_bid")

    def __str__(self):
        return f"{self.user} place bid for:{self.auction}Bid amount ${self.bid_amount}"


class Comment(models.Model):
    comment = models.TextField()
    auction = models.ForeignKey(Auction_listing, on_delete=models.CASCADE, blank=True, null=True, related_name="auction_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_comment")

    def __str__(self):
        return f"{self.user} comment for {self.auction} action: {self.comment}"



