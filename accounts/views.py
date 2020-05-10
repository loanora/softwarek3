from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

#from django.contrib.auth.decorators import login_required #ログインしたユーザーのみに閲覧制限

#@login_required #ログインしたユーザーのみに閲覧制限

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


