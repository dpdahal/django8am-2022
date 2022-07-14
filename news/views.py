from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    data = {
        'newsData': News.objects.all(),
        'categoryData': Category.objects.all(),
    }
    return render(request, 'pages/home/index.html', data)


def about(request):
    data = {
        'title': "About Us"
    }
    return render(request, 'pages/about/about.html', data)


def contact(request):
    return render(request, 'pages/contact/contact.html')
