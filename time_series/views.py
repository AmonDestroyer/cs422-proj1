# Request Handler

from django.shortcuts import render, redirect
from django.http import HttpResponse

def home_page(request):
  return render(request, 'index.html') 

def contributor(request):
  return render(request, 'contributor.html')

def mle(request):
  return render(request, 'mle.html')  

def admin(request):
  return render(request, 'admin.html')  

def _404_handler(request, nonexisting_path):
  return render(request, '404.html')