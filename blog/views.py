from django.shortcuts import render

# Create your views here.
from django.shortcuts import  redirect
from .models import Info
from .forms import InfoForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog_list(request):
    return render(request, 'blog_list.html')