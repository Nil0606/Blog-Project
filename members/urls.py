
from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('update/',views.UserUpdateView.as_view(),name='update'),
    path('password-update/',views.PasswordUpdateView.as_view(),name='password-update'),
]