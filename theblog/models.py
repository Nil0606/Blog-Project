from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")

class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255,default="Nil's Blog",null=True)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    likes=models.ManyToManyField(User,related_name='blog_post')
    date=models.DateTimeField(auto_now_add=True,null=True)
    category=models.CharField(max_length=255,default='Web Developement')

    def __str__(self):
        return self.title+" | "+str(self.auther)

    def get_absolute_url(self):
        return reverse("home")

    def total_likes(self):
        return self.likes.count()
