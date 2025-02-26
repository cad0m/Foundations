from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed",views.closed, name="closed"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("category/<str:name>", views.category, name="category"),
    #these paths for the forms functionality 
    path("listing/<int:id>/add_remove_watchlist", views.add_remove_watchlist, name="add_remove_watchlist"),
    path("listing/<int:id>/place_bid", views.place_bid, name="place_bid"),
    path("listing/<int:id>/close_bid", views.close_bid, name="close_bid"),
    path("listing/<int:id>/add_comment", views.add_comment, name="add_comment"),
]
