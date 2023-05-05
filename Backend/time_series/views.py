from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .upload import upload_set, TRAIN, SOLUTION, TEST
from .download import get_train_data, get_solutions, get_problem_data
from .models import TS_Set

import json

####################################
### Render page request handlers ###
####################################

def redirect_home(request): # Redirect to home page
  return redirect('home/')

def home_page(request): # Render home page
  return render(request, 'index.html') 

def contributor(request): # Render contributor page
  return render(request, 'contributor.html')

def mle(request): # Render mle page
  return render(request, 'mle.html')  

def admin(request): # Render admin page
  return render(request, 'admin.html')  

def login(request): # Render login page
  return redirect('roles:login')

def solution(request): # Render solution page
  return render(request, 'solution.html')


######################################
### Database POST request handlers ###
######################################

# upload training and test data
@csrf_exempt
def upload_data(request):
  """Summary: Uploads a train set, test set, or solution set to the database by calling upload_set and passing in information
  from request.body

  Args:
      request: The request object that contains the data to be uploaded

  Returns:
      HttpResponse: A response object that contains the status of the upload
      Render (redirect): A redirect to the home page if the request is not a POST request
  """
  if request.method == 'POST':
    data_dict = json.loads(request.body) # Load JSON into python dictionary (data)
    
    # Check if a train and test set was uploaded
    # If so, first upload train set
    # uploading train set should return the object that was created
    # then upload test set and pass in the train set object
    if ('trainSet' in data_dict) and ('testSet' in data_dict):
      print("Recieved train and test set")

      # Upload train set
      response = upload_set(data=data_dict['trainSet'], set_type=TRAIN) # Response returned from upload_set
      if (response[0] == 0): # Failed to upload 
        print(response[1])
        return HttpResponse(response[1], status=400) # Return error message with status 400
      
      else: # Upload test set
        response = upload_set(data=data_dict['testSet'], set_type=TEST, train_set=response[1])
        if (response[0] == 0): # Failed to upload
          print(response[1]) 
          return HttpResponse(response[1], status=400) # Return error message with status 400
        else: # Successful upload of both sets
          return HttpResponse('Success', status=200) # Return 'success' message with status 200
    
    # Check if a solution set is being requested to be uploaded
    elif ('ProblemID' in data_dict):
      print("Recieved problem set")

      train_set = TS_Set.objects.get(set_id=data_dict['ProblemID']) # Get the train set object from the database using the problem ID
      response = upload_set(data=data_dict['Solution'], set_type=SOLUTION, train_set=train_set) # Upload solution set, and get response
      
      if (response[0] == 0): # Failed to upload
        return HttpResponse(response[1], status=400)
      else:
        return HttpResponse('Success', status=200)
    
    else:
      print("Not a valid request")
      return HttpResponse('Invalid Request', status=400)

  else: # GET request (or any other) - redirect to home page since this is not a valid request
    return redirect('../home/')
    

@csrf_exempt
def upload_solution(request):
  return upload_data(request) # call upload_data since the functionality is the same (handles solultion upload)


#####################################
### Database GET request handlers ###
#####################################
def train_data_pull_request(request):
  # Gets all train data from the database by calling get_train_data()

  response = get_train_data() # Response is a dictionary containing the train set data
  return JsonResponse(response, status=200, safe=False) # safe=False allows for non-dict objects to be serialized

def download_train_data(request):
  # Gets the train data for a specific problem from the database by calling get_problem_data()
  # Uses request.GET.get('set_id') to get the problem ID which is passed in as a query parameter from the js
  
  set_id = request.GET.get('set_id') # Get the set_id from the GET request
  response = get_problem_data(set_id) # Response is a dictionary containing train data for a specific problem (set_id)
  return JsonResponse(response, status=200, safe=False)

def get_solutions_request(request):
  # Returns back a JSON response containing all solutions in the database by calling get_solutions()

  response = get_solutions() # Response is a dictionary containing all solutions in the database
  return JsonResponse(response, status=200, safe=False)