from django.urls import path
from django.views.generic import RedirectView

from . import views
urlpatterns = [
    path('home/',views.HomeView.as_view(),name="home"),
    path('article/<int:pk>/',views.ArticleDetailView.as_view(),name="article-detail"),
    path('',RedirectView.as_view(url='home/')),
    path('Add_category/',views.AddCategoryView.as_view(),name='add-category'),
    path('Add_post/',views.AddpostView.as_view(),name='add-post'),
    path('categories/<str:cats>/',views.CategoryView,name='category'),
    path('categroies/',views.CategoryListView.as_view(),name='category-list'),
    path('article/edit/<int:pk>/',views.UpadtepostView.as_view(),name="update-post"),
    path('article/<int:pk>/remove/',views.DeletePostView.as_view(),name="delete-post"),
]