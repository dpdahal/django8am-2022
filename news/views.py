from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse


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


def news_details(request, slug):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        parent = request.POST.get('parent')
        if parent:
            cmt = Comments.objects.filter(id=parent).first()
            Comments(news=News.objects.get(slug=slug), name=name, email=email, body=body, parent=cmt).save()
            back = request.META.get("HTTP_REFERER")
            return redirect(back)
        else:
            Comments(news=News.objects.get(slug=slug), name=name, email=email, body=body).save()
            back = request.META.get("HTTP_REFERER")
            return redirect(back)
    else:
        n_obj = News.objects.get(slug=slug)
        related_news = News.objects.filter(category=n_obj.category).exclude(slug=slug)
        n_obj.views += 1
        n_obj.save()
        data = {
            'newsData': News.objects.get(slug=slug),
            'related_news': related_news,
            'commentData': Comments.objects.filter(parent=None)

        }
        return render(request, 'pages/news/news_details.html', data)


def category(request, slug):
    data = {
        'newsData': News.objects.filter(category__category_name=slug),
    }
    return render(request, 'pages/news/category.html', data)
