# Request Handler

from django.shortcuts import render, redirect
from django.http import HttpResponse

def redirect_home(request):
  return redirect('home/')

def home_page(request):
  return render(request, 'index.html') 

def contributor(request):
  return render(request, 'contributor.html')

def mle(request):
  return render(request, 'mle.html')  

def admin(request):
  return render(request, 'admin.html')  

def login(request):
  return redirect('roles:login')