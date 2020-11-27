from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import Registrationform,Updateform,PasswordUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
class UserRegisterView(generic.CreateView):
    form_class =UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    form_class = Updateform
    template_name='registration/update.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordUpdateView(PasswordChangeView):
    form_class =PasswordUpdateForm
    template_name ='registration/password_update.html'
    success_url = reverse_lazy('home')