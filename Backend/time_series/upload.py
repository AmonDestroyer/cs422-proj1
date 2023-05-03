from .models import *
from django.db import transaction
import decimal

from .calculate import calculate_error

# Constants for set_type
TRAIN = 'train' 
SOLUTION = 'solution'
TEST = 'test'
 
def upload_set(data, set_type, train_set=None):
  set_meta = data['setMeta'] # setMeta contains all the set's metadata - set_meta is the dictionary for that metadata
  ts_meta = data['seriesMeta'] # tsMeta contains the time series's metadata - ts_meta is the dictionary for that metadata
  series_data = data['seriesData'] # seriesData contains the time series's data - series_data is the dictionary for that data 
  
  try:
    with transaction.atomic():
      # Create TimeUnit object using TimeUnit object and data from set_meta - add to the database
      # Save the instance of this object to time_unit_instance which will be used for other objects
      time_unit = TimeUnit.objects.create(unit_name='min') 
      
      # This tells what type of set was uploaded (train, test, solution)
      set_type_obj = SetType.objects.create(set_type=set_type) 
      
      # Create TS_Set object using TS_Set object and data from set_meta
      # objects.create() creates the object and then saves it to the database
      # ts_set is an instance of the TS_Set class that is in the database
      ts_set = create_ts_set(data, time_unit, set_type_obj, train_set=train_set)
      
      # Create TimeSeries object using TimeSeries object and data from ts_meta
      # objects.create() creates the object and then saves it to the database
      # ts_timeseries is an instance of the TimeSeries class that is in the database
      timeseries = create_time_series(ts_meta, ts_set)
      
      # loop through all the data in series_data and create a TS_Measurement object for each point
      # each TS_Measurement object will then be created as a row in the Table TS_Measurement in the Database
      # each TS_Measurement object ts_id links it to the timeseries that was created above
      count = 0
      length = int(ts_set.vector_size)
      ts_measurements = []
      
      for _, temp in series_data.items():
        if (count <= length):
          ts_measurement = TS_Measurement(
            x_val = temp,
            ts_id=timeseries
          )
          
          ts_measurements.append(ts_measurement)
          count += 1
        else:
          break
      
      # Bulk add all the objects just created.
      TS_Measurement.objects.bulk_create(ts_measurements)
      
      # Additional meta data for TS_Set that will be joined
      set_domain = Domain.objects.create(domain_name=set_meta['Application Domain(s)'])
      set_keyword = Keyword.objects.create(keyword=set_meta['Keywords'])
      contributor = Contributor.objects.create(contrib_fname=set_meta['Contributors']) # Needs to be fixed later (need to split first and last name)
      paper = Paper.objects.create(paper_reference=set_meta['Related Paper Reference(s)'], paper_link=set_meta['Related Paper Link'])
      
      # Additional meta data for TimeSeries that will be joined
      series_domain = Domain.objects.create(domain_name=ts_meta['Domain(s)'])
      series_keyword = Keyword.objects.create(keyword=ts_meta['Keywords'])
      
      # Set joiners
      TimeseriesSetDomain_Join.objects.create(domain_id=set_domain, set_id=ts_set)
      SetKeyword_Join.objects.create(keyword_id=set_keyword, set_id=ts_set)
      SetContributor_Join.objects.create(contrib_id=contributor, set_id=ts_set)
      SetPaper_Join.objects.create(paper_id=paper, set_id=ts_set)
      
      # TimeSeries joiners
      TimeseriesDomain_Join.objects.create(domain_id=series_domain, ts_id=timeseries)
      TimeseriesKeyword_Join.objects.create(keyword_id=series_keyword, ts_id=timeseries)
      
      if (set_type == TRAIN):
        # 1 indicates success
        return 1, ts_set # TS set needs to be returned so that we can link
      
      else: # if set_type is not "train" then we want to link to the train set
        # Create TestTrainingSolution_Join object using TestTrainingSolution_Join object
        # other_set is the set we just created (see line 30) and we link this to the train set
        TestTrainingSolution_Join.objects.create(training_set_id=train_set, other_set_id=ts_set)
        
        return 1, ts_set # ts_set returned here is the set that was uploaded
 
  except Exception as e:
    return 0, e
  
  
 
def create_ts_set(data, time_unit, set_type_obj, train_set=None):
  set_meta = data['setMeta']
  
  error = None
  if (set_type_obj.set_type == SOLUTION and train_set):
    series_data = data['seriesData']
    error = calculate_error(series_data, train_set.set_id)
    print(error)
  
  ts_set = TS_Set.objects.create(
        set_name=set_meta['TS Set Name'],
        description=set_meta['Description'],
        vector_size=set_meta['Vector Size'],
        min_length=set_meta['Min Length'],
        max_length=set_meta['Max Length'],
        num_ts=set_meta['Number of TS in the Set'],
        start_datetime=set_meta['Start Datetime'],
        error=error, # No error is sent when uploading train/test sets
        tu_id=time_unit,
        set_type_id=set_type_obj
      ) 
  
  return ts_set

# Incomplete? May need to add a loop to create multiple TimeSeries objects
def create_time_series(ts_meta, ts_set):
  timeseries = TimeSeries.objects.create(
        ts_name=ts_meta['TS Name'],
        description=ts_meta['Description'],
        y_unit=ts_meta['Units'],
        scalar_vector=ts_meta['Scalar/Vector'],
        vector_size=ts_meta['Vector Size'],
        length=ts_meta['Length'],
        sampling_period=ts_meta['Sampling Period'],
        error=ts_set.error,
        set_id=ts_set
      )
  
  return timeseries
  
  
  
  
    
  
  
  
  
  
  