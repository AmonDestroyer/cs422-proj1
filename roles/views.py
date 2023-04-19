from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

def login_page(request):
  return render(request, 'login.html')

def redirect_to_time_series(request, role):
  if ('.html' in request.path):
    return redirect(f'time_series:{role}_html') 
  else:
    raise Http404("File not found!")
  
  """elif ('.css' in request.path):
    return redirect(f'time_series:{role}_css')
  elif ('.js' in request.path):
    return redirect(f'time_series:{role}_js')"""
  