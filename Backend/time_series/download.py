import json
from .models import *
from django.db import transaction

import logging

logger = logging.getLogger(__name__)

def get_train_data(request_body):
  
  pass

def get_solutions(request_body):
  # data = json.loads(request_body)
  # set_id = request_body["set_id"]

  set_id = '45' # Temporary for now, above code will be used later
  solutions_dict = {} # Contains all solutions
  solution_dict = {} # Dictionary that will be returned to the frontend (converted to JSON) - stores sollution information
  
  # Get the ts set from the database using set_id
  ts_set = TS_Set.objects.get(set_id=set_id)
  solution_dict.update({
    "set name": ts_set.set_name,
    "error": ts_set.error,
  })
  
  # Get the paper associated with this ts set
  # use setpaper_join__set_id to get the paper associated with ts_set in the Set-Paper Join table
  paper = Paper.objects.get(setpaper_join__set_id=ts_set)
  solution_dict.update({
    "paper reference": paper.paper_reference,
    "paper link": paper.paper_link,
  })
  
  # Get the contributor associated with this ts set
  # use setcontributor_join__set_id to get the contributor associated with ts_set in the Set-Contributor Join table
  contributor = Contributor.objects.get(setcontributor_join__set_id=ts_set)
  # contributor_id = contributor.contrib_id # not used
  solution_dict.update({
    "contributor first name": contributor.contrib_fname,
    "contributor last name": contributor.contrib_lname,
  })
  
  solutions_dict["solution1"] = solution_dict
  print(json.dumps(solutions_dict))

  return ts_set
