import json
from .models import *
from django.db import transaction

from .upload import TRAIN, SOLUTION

def get_problem_data(problem_id=1):
  ts_set = TS_Set.objects.get(set_id=1)
  timeseries = TimeSeries.objects.get(set_id=ts_set)
  ts_data = TS_Measurement.objects.filter(ts_id=timeseries)
  
  domain = Domain.objects.get(timeseriessetdomain_join__set_id=ts_set)
  keywords = Keyword.objects.get(setkeyword_join__set_id=ts_set)
  
  response_dict = {}
  TrainingSet = {}
  SolutionMetadata = {}
  
  setMeta = {}
  
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
  
  for count, data in enumerate(ts_data, start=1):
    key = f"point{count}"
    seriesData[key] = data.x_val
  
  TrainingSet.update({
    "setMeta": setMeta,
    "seriesMeta": seriesMeta,
    "seriesData": seriesData
  })
  
  other_set_ids = TestTrainingSolution_Join.objects.filter(training_set_id=problem_id).values_list('other_set_id', flat=True)
  test_set = TS_Set.objects.get(set_id__in=other_set_ids, set_type_id__set_type='test')
  
  SolutionMetadata.update({
    "Startdate": str(test_set.start_datetime),
    "Units": timeseries.y_unit,
    "Length": timeseries.length,
    "Sampling Period": timeseries.sampling_period,
  })
  
  response_dict.update({
    "TrainingSet": TrainingSet,
    "SolutionMetadata": SolutionMetadata,
  })
  
  return_json = json.dumps(response_dict)
  print(return_json)
  
  return 1


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
