from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    favicon = models.ImageField(upload_to='images/', null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    google = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    intro = RichTextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
