from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

def login_page(request): # Render the login page
  return render(request, 'login.html')

# Redirect to time_series app
def redirect_to_time_series(request, file):
  if ('.html' in request.path):
    return redirect(f'time_series:{file}_html') # Redirect to time_series app, with "file" as the name of the html file
  else:
    raise Http404("File not found!")
  