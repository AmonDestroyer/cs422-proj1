from django.db import connection

from sklearn.metrics import mean_squared_error
from .models import *

def calculate_error(solution_data, train_set_id):
  # Get all the ids of sets linked to the train_set_id
  # other_set_ids will contain a <QuerySet> object containing the other_set_ids
  # these ids are only the ids of the sets that are linked with train_set_id
  other_set_ids = TestTrainingSolution_Join.objects.filter(training_set_id=train_set_id).values_list('other_set_id', flat=True)
  
  # To get the test_set, we use set_id__in to get all the objects that have set_id in other_set_ids
  # We then get using set_type_id__set_type='test' to get only the test set among the other_set_ids
  test_set = TS_Set.objects.get(set_id__in=other_set_ids, set_type_id__set_type='test')
  test_ts = TimeSeries.objects.get(set_id=test_set)
  
  ts_measurements = TS_Measurement.objects.filter(ts_id=test_ts)
  true_data = []
  
  for measurement in ts_measurements:
    true_data.append(measurement.x_val)
  
  # Convert solution_data to a list of integers
  # Sollution data is a dictionary such as {'key': '1',...}
  pred_data = [int(solution_data[key]) for key in solution_data]
  
  if len(pred_data) == len(true_data):
    error = mean_squared_error(true_data, pred_data)
    print(error)
    
    return mean_squared_error(true_data, pred_data)
  
  else:
    return -1
  