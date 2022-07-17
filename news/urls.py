from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact-us', views.contact, name='contact-us'),
    path('news-details/<slug>',views.news_details, name='news-details'),
    path('category/<slug>',views.category, name='category'),
]
