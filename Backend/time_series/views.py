# Request Handler
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.http import HttpResponse

# from upload import upload_file

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


# upload file (training + test data) - POST request handler
@csrf_exempt
def upload_data(request):
  if request.method == 'POST':

    jsonStr = request.body
    print(jsonStr)
    # call function to process uploaded file - send request.body to function

    return render(request, 'contributor.html')
    


  else: # GET request - redirect to home page since this is not a valid request
    return redirect('../home/')