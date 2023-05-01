import json
from .models import *
from django.db import transaction

from .upload import TRAIN, SOLUTION

def get_train_data():
  # Get all the train sets from the database
  
  ts_training_sets = TS_Set.objects.filter(set_type_id__set_type=TRAIN)
  
  response_dict = {}
  count = 1
  
  for ts_set in ts_training_sets:
    set_info = {}
    set_info.update({
      "set id": ts_set.set_id,
      "set name": ts_set.set_name
    })
    
    paper = Paper.objects.get(setpaper_join__set_id=ts_set)
    
    set_info.update({
      "paper reference": paper.paper_reference,
      "paper link": paper.paper_link
    })
    
    contributor = Contributor.objects.get(setcontributor_join__set_id=ts_set)
    
    set_info.update({
      "contributor first name": contributor.contrib_fname,
      "contributor last name": contributor.contrib_lname
    })
    
    response_dict[f"set{count}"] = set_info
    count += 1
  
  return_json = json.dumps(response_dict)
  print(return_json)
  
  return return_json

def get_solutions(request_body):
  # data = json.loads(request_body)
  # set_id = request_body["set_id"]

  set_id = '1' # Temporary for now, above code will be used later
  solutions_dict = {} # Contains all solutions
  count = 1
  
  # Get the ts set from the database using set_id
  # ts_set = TS_Set.objects.get(set_id=set_id)
  
  solution_sets = TS_Set.objects.filter(set_type_id__set_type=SOLUTION) #, testtrainingsolution_join__training_set_id=set_id)
  
  for solution in solution_sets:
    solution_info = {} # Dictionary that will be returned to the frontend (converted to JSON) - stores sollution information
    solution_info.update({
      "set name": solution.set_name,
      "error": str(solution.error), # conver to string because JSOn doesn't accept DECIMAL
    })
    
    # Get the paper associated with this ts set
    # use setpaper_join__set_id to get the paper associated with ts_set in the Set-Paper Join table
    paper = Paper.objects.get(setpaper_join__set_id=solution)
    solution_info.update({
      "paper reference": paper.paper_reference,
      "paper link": paper.paper_link,
    })
    
    # Get the contributor associated with this ts set
    # use setcontributor_join__set_id to get the contributor associated with ts_set in the Set-Contributor Join table
    contributor = Contributor.objects.get(setcontributor_join__set_id=solution)
    # contributor_id = contributor.contrib_id # not used
    solution_info.update({
      "contributor first name": contributor.contrib_fname,
      "contributor last name": contributor.contrib_lname,
    })
  
    solutions_dict[f"solution{count}"] = solution_info
    count += 1
  
  return_json = json.dumps(solutions_dict)
  print(return_json)

  return return_json
