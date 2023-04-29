from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .upload import upload_set, TRAIN, SOLUTION, TEST
from .download import get_train_data, get_solutions
from .calculate import calculate_error

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
      
      else:
        response = upload_set(data=data_dict['testSet'], set_type=TEST, train_set=response[1])
        if (response[0] == 0):
          print(response[1])
          return HttpResponse(response[1], status=400)
        else:
          return HttpResponse('Success', status=200)
    
    # Check if a solution set was uploaded
    # If so, calculate error then upload solution set
    elif ('ProblemID' in data_dict):
      print("Recieved problem set")
      return HttpResponse('Not-Implemented', status=200)

  else: # GET request (or any other) - redirect to home page since this is not a valid request
    return redirect('../home/')
    

@csrf_exempt
def upload_solution(request):
  if request.method == 'POST':
    jsonStr = request.body
    
    # Upload the solution set
    # Need to make sure to pass in the ts_set_id of the train set
    # request.body: {"ts set id": "num", "solution": "{data}"}
    # might need to change around upload_set slightly so i can get both in
    response = upload_set(jsonStr)
    
    # Response 1 will contain ts_set of the solution that was pushed
    error = calculate_error(jsonStr["ts set id"], response[1])
    
    return HttpResponse('Success', status=200)
  else: # GET request (or any other) - redirect to home page since this is not a valid request
    return redirect('../home/')


### Database GET request handlers ###
def train_data_download_request(request):
  response = get_train_data(request.body)


def get_solutions_request(request):
  # request.body should be a json object containing set_id
  response = get_solutions(request.body)
  return HttpResponse('Success', status=200)