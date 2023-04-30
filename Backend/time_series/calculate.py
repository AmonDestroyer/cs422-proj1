from django.db import connection

from sklearn.metrics import mean_squared_error
from .models import *

def calculate_error(solution_data, train_set_id):
  # First need to get the test set data 
  # Test set data is linked to the train_set
  print(train_set_id)

  # Currently impossible to get the test set data
  
  return 1 # mean_squared_error(1, 1)
  