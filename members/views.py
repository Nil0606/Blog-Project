from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import Registrationform
class UserRegisterView(generic.CreateView):
    form_class =Registrationform
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
