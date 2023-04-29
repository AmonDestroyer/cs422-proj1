# Request Handler
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .upload import upload_train_test_to_db
from .download import get_train_data, get_solutions

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
    # print(jsonStr)
    
    # call function to process uploaded file - send request.body to function
    response = upload_train_test_to_db(jsonStr)
    
    if response[0] == 0:
      print(response[1])
      return HttpResponse(response[1], status=400)
    else:
      # return render(request, 'contributor.html')
      return HttpResponse(response[1], status=200)

  else: # GET request - redirect to home page since this is not a valid request
    return redirect('../home/')


def train_data_download_request(request):
  response = get_train_data(request.body)


def get_solutions_request(request):
  # request.body should be a json object containing set_id
  response = get_solutions(request.body)
  return HttpResponse('Success', status=200)