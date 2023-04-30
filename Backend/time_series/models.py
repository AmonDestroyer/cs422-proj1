from django.db import models

# Create your models here.
# All models (classes) follow the sql schema created from our sql file
# All models will be used to create a python object which will then be passed into the database as a row to
# their respective tables

class TimeUnit(models.Model):
  tu_id = models.AutoField(primary_key=True) # Creates an auto-incrementing primary key (starts at 1)
  unit_name = models.CharField(max_length=1000, null=True) # 
  
  class Meta:
    db_table = 'Time Unit' # Used to specify the name of the table in the database


class SetType(models.Model):
  set_type_id = models.AutoField(primary_key=True)
  set_type = models.CharField(max_length=1000, null=True)

  class Meta:
    db_table = 'Set Type'


class TS_Set(models.Model):
  set_id = models.AutoField(primary_key=True)
  set_name = models.CharField(max_length=1000, null=True)
  description = models.CharField(max_length=1000, null=True)
  vector_size = models.IntegerField(null=True)
  min_length = models.IntegerField(null=True)
  max_length = models.IntegerField(null=True)
  num_ts = models.IntegerField(null=True)
  start_datetime = models.DateTimeField(null=True)
  error = models.FloatField(null=True)
  tu_id = models.ForeignKey(TimeUnit, on_delete=models.DO_NOTHING, db_column='tu_id')
  set_type_id = models.ForeignKey(SetType, on_delete=models.DO_NOTHING, db_column='set_type_id')

  class Meta:
    db_table = 'TS_Set'


class TimeSeries(models.Model):
  ts_id = models.AutoField(primary_key=True)
  ts_name = models.CharField(max_length=1000, null=True)
  description = models.CharField(max_length=1000, null=True)
  y_unit = models.CharField(max_length=1000, null=True)
  scalar_vector = models.SmallIntegerField(null=True, db_column='scalar/vector')
  vector_size = models.IntegerField(null=True)
  length = models.IntegerField(null=True)
  sampling_period = models.IntegerField(null=True)
  error= models.FloatField(null=True)
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='set_id')
  
  class Meta:
    db_table = 'Time Series'
    

class Keyword(models.Model):
  keyword_id = models.AutoField(primary_key=True)
  keyword = models.CharField(max_length=1000, null=True)
  
  class Meta:
    db_table = 'Keyword'


class Contributor(models.Model):
  contrib_id = models.AutoField(primary_key=True)
  contrib_fname = models.CharField(max_length=1000, null=True)
  contrib_lname = models.CharField(max_length=1000, null=True)
  
  class Meta:
    db_table = 'Contributor'


class Domain(models.Model):
  domain_id = models.AutoField(primary_key=True)
  domain_name = models.CharField(max_length=1000, null=True)
  
  class Meta:
    db_table = 'Domain'

 
class Paper(models.Model):
  paper_id = models.AutoField(primary_key=True)
  paper_reference = models.CharField(max_length=1000, null=True)
  paper_link = models.CharField(max_length=1000, null=True)
  
  class Meta:
    db_table = 'Paper'


class SetKeyword_Join(models.Model):
  keyword_id = models.ForeignKey(Keyword, on_delete=models.DO_NOTHING, db_column='keyword_id')
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='set_id')
  
  class Meta:
    db_table = 'Set-Keyword_Join'


class SetContributor_Join(models.Model):
  contrib_id = models.ForeignKey(Contributor, on_delete=models.DO_NOTHING, db_column='contrib_id')
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='set_id')
  
  class Meta:
    db_table = 'Set-Contributor_Join'
    

class SetPaper_Join(models.Model):
  paper_id = models.ForeignKey(Paper, on_delete=models.DO_NOTHING, db_column='paper_id')
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='set_id')
  
  class Meta:
    db_table = 'Set-Paper_Join'


class TimeseriesKeyword_Join(models.Model):
  keyword_id = models.ForeignKey(Keyword, on_delete=models.DO_NOTHING, db_column='keyword_id')
  ts_id = models.ForeignKey(TimeSeries, on_delete=models.DO_NOTHING, db_column='ts_id')

  class Meta:
    db_table = 'Timeseries-Keyword_Join'
    

class TS_Measurement(models.Model):
  tsm_id = models.AutoField(primary_key=True)
  x_val = models.IntegerField(null=True)
  y_val = models.FloatField(null=True)
  ts_id = models.ForeignKey(TimeSeries, on_delete=models.DO_NOTHING, db_column='ts_id')
  
  class Meta:
    db_table = 'TS_Measurement'


class TimeseriesDomain_Join(models.Model):
  domain_id = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, db_column='domain_id')
  ts_id = models.ForeignKey(TimeSeries, on_delete=models.DO_NOTHING, db_column='ts_id')
  
  class Meta:
    db_table = 'Timeseries-Domain_Join'


class TimeseriesSetDomain_Join(models.Model):
  domain_id = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, db_column='domain_id')
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='set_id')
  
  class Meta:
    db_table = 'TimeseriesSet-Domain_Join'


# Link/Bridge test and training TS sets together
class TestTrainingSolution_Join(models.Model):
  training_set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='training_set_id', related_name='training_set_id')
  other_set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='other_set_id', related_name='other_set_id')

  class Meta:
    db_table = 'Test-Training-Solution_Join'
    unique_together = (('training_set_id', 'other_set_id'),)
