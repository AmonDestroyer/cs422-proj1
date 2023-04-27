from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

def login_page(request):
  return render(request, 'login.html')

def redirect_to_time_series(request, file):
  if ('.html' in request.path):
    return redirect(f'time_series:{file}_html') 
  else:
    raise Http404("File not found!")
  