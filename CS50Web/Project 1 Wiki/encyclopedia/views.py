from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from . import util
import markdown2
import random

class Newentry(forms.Form):
    title = forms.CharField(label='',  widget= forms.TextInput(attrs={'placeholder':'enter title', 'class':'title'}))
    content = forms.CharField(label='', widget= forms.Textarea(attrs={'placeholder':'enter content in markdown', 'class':'content'}))

## views
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name, check= False):
    couldbe = []
    for item in util.list_entries():
        if name.lower() == item.lower():
            return render(request, "encyclopedia/entry.html", {
                "titlee": item,
                "content": markdown2.markdown(util.get_entry(item)),
            })
        elif name.lower() in item.lower():
            couldbe.append(item)
    
    if check :
        return render(request, "encyclopedia/search.html", {
            "userinput": name,
            "maybe": couldbe,
            "empty": not bool(couldbe)
        })

    return render(request, "encyclopedia/error.html", {
        "ErrorType": 'notexist',
        "title": name,
    })

def search(request):
    if request.method == "POST":
        name = request.POST['q']
        return entry(request, name, True)
        
def create(request):
    titles = []
    for item in util.list_entries():
        titles.append(item.lower())
    
    if request.method == "POST": 
        form = Newentry(request.POST)
        if form.is_valid() :
            
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            if title.lower() not in titles:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry", kwargs={'name': title}))
            else:
                return render(request, "encyclopedia/error.html", {
                "ErrorType": 'exist',
                "title": title,
                })
        else:
            return render(request, "encyclopedia/create.html", {
            "form" : form
            })
    return render(request, "encyclopedia/create.html", {
        "form" : Newentry()
    })

def edit(request, titlee):
    if request.method == "POST": 
        form = Newentry(request.POST)
        if form.is_valid() :
            
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
        
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={'name': title}))
            
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": titlee,
            "form": Newentry(initial={"title": titlee, "content": util.get_entry(titlee)})
        })

def random_page(request):
    selected = random.choice(util.list_entries())
    return entry(request, selected)