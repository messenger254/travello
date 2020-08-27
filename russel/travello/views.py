from django.shortcuts import render
from .models import Destination

# Create your views here.
# def index(request):
#     dests = Destination.objects.all()
#     return render (request,"index.html",{'dests':dests} )


def home(request):
    dests = Destination.objects.all()
    return render (request,"travello/index.html",{'dests':dests} )

def contact(request):
    return render(request,"travello/contact.html" )

def about(request):
    return render(request,"travello/about.html")

def news(request):
    return render(request,"travello/news.html")
