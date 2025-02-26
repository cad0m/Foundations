from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
   pass

class Listing(models.Model):
    categories_list = [
    ("1", "Art"),
    ("2", "Books"),
    ("3", "Collectibles"),
    ("4", "Electronics"),
    ("5", "Fashion"),
    ("6", "Home"),
    ("7", "Sports"),
    ("8", "Toys"),
    ("9", "Vehicles"),
    ("10", "Food"),
    ("11", "Other")
    ]
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=300, choices=categories_list)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    current_bid = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    number_of_bids =  models.PositiveIntegerField(default=0)
    listing_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    image_url = models.URLField(max_length=256, blank=True, null=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="winnners", null=True)

    # method to set the current bid = to the starting bid 
    # if self.pk mean its a new item to the Listing 
    def save(self, *args, **kwargs):
        if not self.pk:
            self.current_bid = self.starting_bid
        super().save(*args, **kwargs)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="Listing")
    
    #a method to ensure that every user add only once an unique item to his watchlist
    class Meta:
        unique_together = ('user', 'listing')

class Comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    commented_on = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment_date = models.DateField(auto_now_add=True) # this auto add the current time when the user submit the comment
    comment = models.TextField()                           

class Bids(models.Model):
    bider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_on = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bid_date = models.DateField(auto_now_add=True) # this auto add the current time when the user submit the bid
    bid_value = models.DecimalField(max_digits=9, decimal_places=2)