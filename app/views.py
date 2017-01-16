"""
Definition of views.
"""

from django.shortcuts import render , get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Post
from django.utils import timezone


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'app/post_list.html',{'posts': posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_details.html', {'post': post})