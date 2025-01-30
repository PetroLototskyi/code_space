from django.urls import path
from django.contrib import admin


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("admin/", admin.site.urls),
    path('selected_category', views.selected_category, name="selected_category"),
    path("item/<int:id>", views.item, name="item"),
    path("remove_watch/<int:id>", views.remove_watch, name="remove_watch"),
    path("add_watch/<int:id>", views.add_watch, name="add_watch"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_comment/<int:id>", views.add_comment, name="add_comment"),
    path("add_bid/<int:id>", views.add_bid, name="add_bid"),
    path("close_auction/<int:id>", views.close_auction, name="close_auction"),
    path("won_auction", views.won_auction, name="won_auction")
]
