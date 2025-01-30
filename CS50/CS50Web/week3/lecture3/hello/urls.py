from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"), #"" - empty string means no additional argument; name - is optional
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david")

]
