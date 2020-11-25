from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255,default="Nil's Blog",null=True)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    likes=models.ManyToManyField(User,related_name='blog_post')
    date=models.DateTimeField(auto_now_add=True,null=True)
    snippet=models.TextField(default='First blog')
    category=models.CharField(max_length=255,default='Web Developement')

    def __str__(self):
        return self.title+" | "+str(self.auther)

    def get_absolute_url(self):
        return reverse("home")

    def total_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=150)
    first_name=models.CharField(max_length=150,null=True)
    last_name=models.CharField(max_length=150)
    bio=models.CharField(max_length=300)
    image=models.ImageField(null=True,blank=True,upload_to="profile_image/",default="default.png")


