import json
from .models import *
from django.db import transaction

from .upload import TRAIN, SOLUTION

def get_problem_data(problem_id):
  """Gets all the information associated with problem_id from the database. Additionally, gets the necessary information for how the solution set
     should be formatted based on how the test set for the problem is formatted.

  Args:
      problem_id (int): The id of the TS_Set to be downloaded (retrieved from the database).

  Returns:
      dict: Returns a dictionary containing all the information associated with problem_id as well as solution metadata (how it should be formatted)
  """
  
  ts_set = TS_Set.objects.get(set_id=problem_id) # Gets TS_Set from database with problem_id
  timeseries = TimeSeries.objects.get(set_id=ts_set) # Gets timeseries associated with ts_set
  ts_data = TS_Measurement.objects.filter(ts_id=timeseries) # Gets all ts_data associated with timeseries
  
  domain = Domain.objects.get(timeseriessetdomain_join__set_id=ts_set)
  keywords = Keyword.objects.get(setkeyword_join__set_id=ts_set)
  
  # Dictionaries that will be used to store and format the data so it can be returned to the frontend as a proper JSON object
  response_dict = {}
  TrainingSet = {}
  SolutionMetadata = {}
  
  setMeta = {}
  
  # Use ts.set's attributes to populate setMeta
  setMeta.update({
    "TS Set Name": ts_set.set_name,
    "Description": ts_set.description,
    "Aplication Domain(s)": domain.domain_name,
    "Keywords": keywords.keyword,
    "Vector Size": ts_set.vector_size,
    "Min Length": ts_set.min_length,
    "Max Length": ts_set.max_length,
    "Number of TS in the Set": ts_set.num_ts,
    "Start Datetime": str(ts_set.start_datetime),
  })
  
  seriesMeta = {}
  
  # Use timeseries's attributes to populate seriesMeta
  seriesMeta.update({
    "TS Name": timeseries.ts_name,
    "Description": timeseries.description,
    "Units": timeseries.y_unit,
    "Scalar/Vector": timeseries.scalar_vector,
    "Vector Size": timeseries.vector_size,
    "Length": timeseries.length,
    "Sampling Period": timeseries.sampling_period,
  })
  
  seriesData = {}
  
  # Use ts_data to populate seriesData
  for count, data in enumerate(ts_data, start=1):
    key = f"point{count}"
    seriesData[key] = data.x_val
  
  # Use the dictionaries to populate the TrainingSet dictionary
  TrainingSet.update({
    "setMeta": setMeta,
    "seriesMeta": seriesMeta,
    "seriesData": seriesData
  })
  
  # Get the test set associated with the problem set
  # Given the problem id, we can get the test set using .values_list('other_set_id', flat=True) to get all of the other_set_ids
  # linked to the problem id. flat=True makes it so it returns a list of ids instead of a list of tuples associated with 'other_set_id'
  # The test_set then can be retrieved using .get and filtering by set_id__in=other_set_ids and set_type_id__set_type='test'
  # We know only one TS_Set will be returned since there is only one test set associated with a problem set
  other_set_ids = TestTrainingSolution_Join.objects.filter(training_set_id=problem_id).values_list('other_set_id', flat=True)
  test_set = TS_Set.objects.get(set_id__in=other_set_ids, set_type_id__set_type='test')
  
  # Store solution metadata so a proper solution can be created matching the test set
  SolutionMetadata.update({
    "Startdate": str(test_set.start_datetime),
    "Units": timeseries.y_unit,
    "Length": timeseries.length,
    "Sampling Period": timeseries.sampling_period,
  })
  
  # Add the dictionaries to the response_dict
  response_dict.update({
    "TrainingSet": TrainingSet,
    "SolutionMetadata": SolutionMetadata,
  })
  
  # print(json.dumps(response_dict))
  return response_dict


def get_train_data():
  """Gets all the train sets from the database

  Returns:
      dict: A dictionary containing all the train sets and the necessary information to be displayed on the frontend
  """
  
  # Filter all TS_Sets based on their set_type being TRAIN
  ts_training_sets = TS_Set.objects.filter(set_type_id__set_type=TRAIN)
  
  response_dict = {}
  count = 1 # Count used to number each set
  
  for ts_set in ts_training_sets:
    set_info = {}
    set_info.update({
      "set id": ts_set.set_id,
      "set name": ts_set.set_name
    })
    
    paper = Paper.objects.get(setpaper_join__set_id=ts_set)
    
    set_info.update({
      "paper reference": paper.paper_reference,
      "paper link": (paper.paper_link)
    })
    
    contributor = Contributor.objects.get(setcontributor_join__set_id=ts_set)
    
    set_info.update({
      "contributor first name": contributor.contrib_fname,
      "contributor last name": contributor.contrib_lname
    })
    
    response_dict[f"set{count}"] = set_info
    count += 1
    
  # print(json.dumps(response_dict))
  
  return response_dict


def get_solutions():
  """Gets all solutions from the database and returns them in a dictionary

  Returns:
      dict: Dictionary containing all solutions (sorted by error) with the necessary information to display on the frontend
  """
  
  # Get all the ids of sets linked to the train_set_id
  # other_set_ids will contain a <QuerySet> object containing the other_set_ids
  # these ids are only the ids of the sets that are linked with train_set_id
  problem_sets = TS_Set.objects.filter(set_type_id__set_type=TRAIN)
  
  problem_solutions_dict = {}
  problem_count = 1

  for problem_set in problem_sets:
    solutions_dict = {} # Contains solutions for this problem_set
    solution_count = 1 # Used to number each solultion for this problem_set
    
    # Get all the ids of sets linked to the train_set_id
    # flat=True makes it so a list of ids is returned instead of a list of tuples associated with 'other_set_id' 
    other_set_ids = TestTrainingSolution_Join.objects.filter(training_set_id=problem_set.set_id).values_list('other_set_id', flat=True)
    
    # Get all solution sets where set_id is in other_set_ids
    # solution_sets will be linked to the problem_set because they are in other_set_ids
    # We also know they'll be all the solution sets because their set_type is filtered as SOLUTION
    solution_sets = TS_Set.objects.filter(set_id__in=other_set_ids, set_type_id__set_type=SOLUTION)
    
    for solution in solution_sets:
      solution_info = {} # Dictionary that will be returned to the frontend - stores sollution information
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
      solution_info.update({
        "contributor first name": contributor.contrib_fname,
        "contributor last name": contributor.contrib_lname,
      })
    
      solutions_dict[f"solution{solution_count}"] = solution_info
      solution_count += 1
    
    problem_solutions_dict[f"{problem_set.set_id}"] = solutions_dict
    problem_count += 1
  
  # Sort based on error:
  for key in problem_solutions_dict:
    problem_solutions_dict[key] = dict(sorted(problem_solutions_dict[key].items(), key=lambda item: item[1]["error"]))
  
  # print(json.dumps(problem_solutions_dict))

  return problem_solutions_dict 
