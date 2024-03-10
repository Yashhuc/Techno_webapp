from django.shortcuts import render
from .models import Post

# Create your views here.


# This function is going to handle the traffic from homepage of our blog
def home(request):
    context={
        "posts":Post.objects.all() # get all posts from database
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':"About Us"})

def contact(request):
    return render(request, 'blog/contact.html', {'title':"Contact Us"})