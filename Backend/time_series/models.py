from django.db import models

# Create your models here.

class TimeUnit(models.Model):
  tu_id = models.IntegerField(primary_key=True)
  unit_name = models.CharField(max_length=45, null=True)
  
  class Meta:
    db_table = 'Time Unit'


class TS_Set(models.Model):
  set_id = models.IntegerField(primary_key=True)
  set_name = models.CharField(max_length=200, null=True)
  description = models.CharField(max_length=1000, null=True)
  vector_size = models.IntegerField(null=True)
  min_length = models.IntegerField(null=True)
  max_length = models.IntegerField(null=True)
  num_ts = models.IntegerField(null=True)
  time_unit = models.ForeignKey(TimeUnit, on_delete=models.DO_NOTHING, db_column='Time Unit_tu_id')


class TimeSeries(models.Model):
  ts_id = models.IntegerField(primary_key=True)
  ts_name = models.CharField(max_length=100, null=True)
  description = models.CharField(max_length=1000, null=True)
  y_unit = models.CharField(max_length=45, null=True)
  scalar_vector = models.SmallIntegerField(null=True, db_column='scalar/vector')
  vector_size = models.IntegerField(null=True)
  length = models.IntegerField(null=True)
  sampling_period = models.IntegerField(null=True)
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='TS_Set_set_id')
  
  class Meta:
    db_table = 'Time Series'
  

class Keyword(models.Model):
  keyword_id = models.IntegerField(primary_key=True)
  keyword = models.CharField(max_length=100, null=True)


class Contributor(models.Model):
  contrib_id = models.IntegerField(primary_key=True)
  contrib_fname = models.CharField(max_length=100, null=True)
  contrib_lname = models.CharField(max_length=100, null=True)


class Domain(models.Model):
  domain_id = models.IntegerField(primary_key=True)
  domain_name = models.CharField(max_length=1000, null=True)


class Paper(models.Model):
  paper_id = models.IntegerField(primary_key=True)
  paper_reference = models.CharField(max_length=1000, null=True)
  paper_link = models.CharField(max_length=1000, null=True)


class SetKeyword_Join(models.Model):
  keyword_id = models.ForeignKey(Keyword, on_delete=models.DO_NOTHING, db_column='Keyword_keyword_id')
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='TS_Set_set_id')
  
  class Meta:
    db_table = 'Set-Keyword_Join'


class SetContributor_Join(models.Model):
  contrib_id = models.ForeignKey(Contributor, on_delete=models.DO_NOTHING, db_column='Contributor_contrib_id')
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='TS_Set_set_id')
  
  class Meta:
    db_table = 'Set-Contributor_Join'
    

class SetPaper_Join(models.Model):
  paper_id = models.ForeignKey(Paper, on_delete=models.DO_NOTHING, db_column='Paper_paper_id')
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='TS_Set_set_id')
  
  class Meta:
    db_table = 'Set-Paper_Join'


class TimeseriesKeyword_Join(models.Model):
  ts_id = models.ForeignKey(TimeSeries, on_delete=models.DO_NOTHING, db_column='Time Series_ts_id')
  keyword_id = models.ForeignKey(Keyword, on_delete=models.DO_NOTHING, db_column='Keyword_keyword_id')
  
  class Meta:
    db_table = 'Timeseries-Keyword_Join'
    

class TS_Measurement(models.Model):
  tsm_id = models.IntegerField(primary_key=True)
  x_val = models.IntegerField(null=True)
  y_val = models.FloatField(null=True)
  ts_id = models.ForeignKey(TimeSeries, on_delete=models.DO_NOTHING, db_column='Time Series_ts_id')
  

class TimeseriesDomain_Join(models.Model):
  domain_id = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, db_column='Domain_domain_id')
  ts_id = models.ForeignKey(TimeSeries, on_delete=models.DO_NOTHING, db_column='Time Series_ts_id')
  
  class Meta:
    db_table = 'Timeseries-Domain_Join'


class TimeseriesSetDomain_Join(models.Model):
  set_id = models.ForeignKey(TS_Set, on_delete=models.DO_NOTHING, db_column='TS_Set_set_id')
  domain_id = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, db_column='Domain_domain_id')
  
  class Meta:
    db_table = 'TimeseriesSet-Domain_Join'