from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from .forms import *
from django.http import HttpResponseRedirect

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
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleDetailView, self).get_context_data()
        context['cat_menu']=cat_menu
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        total_likes=stuff.total_likes()
        context['total_likes']=total_likes
        context['liked']=liked
        return context

def Likeview(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse_lazy('article-detail',args=[str(pk)]))

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



