from django.contrib import admin
from .models import User, Auction_listing, Bid, Comment, Category
from django.contrib.auth.admin import UserAdmin

class AuctionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "current_price", "owner", "category")
    list_display_links = ("id", "name")  # Make both "id" and "name" clickable

class   BidAdmin(admin.ModelAdmin):
    list_display = ("id", "bid_amount", "auction", "user")
    list_display_links = ("id", "bid_amount")

class   CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "auction", "comment")
    list_display_links = ("id", "user")

admin.site.register(Auction_listing, AuctionAdmin)
admin.site.register(User, UserAdmin)  # Register the default User model
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)


