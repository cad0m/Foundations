from django.contrib import admin
from .models import User, Listing, Comment, Bids, Watchlist
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")

class ListingAdmin(admin.ModelAdmin):
    list_display= ("id", "poster", "title", "category", "starting_bid", "current_bid", "number_of_bids", "winner","status")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "commentor", "commented_on_post", "comment_date", "comment")
    
    #ensure that the commented_on_post show the listing title not his id 
    def commented_on_post(self, obj):
        return obj.commented_on.title
    
    #this render post name instead of commented_on_post (it make it short)
    commented_on_post.short_description = 'post name'
        
class BidsAdmin(admin.ModelAdmin):
    list_display = ("id", "bider", "bid_on_title", "bid_value", "bid_date")
    
    #ensure that the bid_on_title  show the listing title not his id
    def bid_on_title(self, obj):
        return obj.bid_on.title
    
    bid_on_title.short_description = 'Bid On'


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("user", "listing")

admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(Watchlist, WatchlistAdmin)