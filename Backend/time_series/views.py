from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .upload import upload_set, TRAIN, SOLUTION, TEST
from .download import get_train_data, get_solutions, get_problem_data
from .models import TS_Set

import json

### Render page request handlers ###
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

def solution(request):
  return render(request, 'solution.html')


### Database POST request handlers ###

# upload training and test data
@csrf_exempt
def upload_data(request):
  if request.method == 'POST':
    data_dict = json.loads(request.body) # Load JSON into python dictionary (data)
    
    # Check if a train and test set was uploaded
    # If so, first upload train set
    # uploading train set should return the object that was created
    # then upload test set and pass in the train set object
    if ('trainSet' in data_dict) and ('testSet' in data_dict):
      print("Recieved train and test set")

      # Upload train set
      response = upload_set(data=data_dict['trainSet'], set_type=TRAIN)
      if (response[0] == 0): # Failed to upload 
        print(response[1])
        return HttpResponse(response[1], status=400)
      
      else: # Upload test set
        response = upload_set(data=data_dict['testSet'], set_type=TEST, train_set=response[1])
        if (response[0] == 0): # Failed to upload
          print(response[1])
          return HttpResponse(response[1], status=400)
        else: # Successful upload of both sets
          return HttpResponse('Success', status=200)
    
    # Check if a solution set is being requested to be uploaded
    elif ('ProblemID' in data_dict):
      print("Recieved problem set")
      # Not sure how I feel about pulling from the db in this function
      # However currently this will have to do
      train_set = TS_Set.objects.get(set_id=data_dict['ProblemID']) 
      response = upload_set(data=data_dict['Solution'], set_type=SOLUTION, train_set=train_set)
      
      if (response[0] == 0): # Failed to upload
        return HttpResponse(response[1], status=400)
      else:
        return HttpResponse('Success', status=200)

  else: # GET request (or any other) - redirect to home page since this is not a valid request
    return redirect('../home/')
    

@csrf_exempt
def upload_solution(request):
  return upload_data(request)


### Database GET request handlers ###
def train_data_pull_request(request):
  response = get_train_data()
  return HttpResponse('Success', status=200)


def download_train_data(request):
  response = get_problem_data()
  return HttpResponse('Success', status=200)


def get_solutions_request(request):
  # request.body should be a json object containing set_id
  response = get_solutions()
  return JsonResponse(response, status=200, safe=False) # safe=False allows for non-dict objects to be serialized