from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Listing, Comment, Bids, User

class NewListing(forms.ModelForm):
    class Meta:
        model = Listing #the model that the form inherit form it 
        fields =["title", "category", "description", "starting_bid", "image_url"] 
        exclude = ['poster']
    image_url = forms.URLField(required=False)

class NewComment(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ["comment"]
      exclude = ["commentor", "commented_on"]

class NewBids(forms.ModelForm):
    class Meta:
        model = Bids
        fields = ["bid_value"]
        exclude = ["bider", "bid_on"]

    #that a way to get the lisiting that the bid is submit on it 
    def __init__(self, *argv, **kwargs):
        self.listing = kwargs.pop('listing', None)
        super().__init__(*argv, **kwargs)
        self.fields['bid_value'].widget.attrs.update({'class': 'form-control form-control-lg'})
    
    #valid the input if invalid return a message
    def clean_bid_value(self):
        bid_value = self.cleaned_data.get('bid_value')
        if bid_value <= self.listing.current_bid:
            raise forms.ValidationError("Your bid must be higher than the current bid.")
        print("clean_bid", bid_value)
        return bid_value