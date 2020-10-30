from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from .forms import *

class HomeView(ListView):
    model = models.Post
    template_name = 'home.html'
    ordering = ['-date']
    def get_context_data(self):
        cat_menu=Category.objects.all()
        context=super(HomeView, self).get_context_data()
        context['cat_menu']=cat_menu
        return context

class ArticleDetailView(DetailView):
    model=models.Post
    template_name = 'article_detail.html'


class AddpostView(CreateView):
    model=models.Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model=models.Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request,cats):
    category_post=models.Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.replace('-',' '),'category_post':category_post})

class CategoryListView(ListView):
    model=Category
    template_name = 'category-list.html'
    ordering = ['-id']

class UpadtepostView(UpdateView):
    model=models.Post
    form_class =UpdateForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model=models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



