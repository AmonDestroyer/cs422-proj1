from django.db import models

# Create your models here.

class Time_Unit(models.Model):
  tu_id = models.IntegerField(primary_key=True)
  unit_name = models.CharField(max_length=45, null=True)

class TS_Set(models.Model):
  set_id = models.IntegerField(primary_key=True)
  set_name = models.CharField(max_length=200, null=True)
  description = models.CharField(max_length=1000, null=True)
  vector_size = models.IntegerField(null=True)
  min_length = models.IntegerField(null=True)
  max_length = models.IntegerField(null=True)
  num_ts = models.IntegerField(null=True)
  time_unit = models.ForeignKey(Time_Unit, on_delete=models.DO_NOTHING, db_column='Time Unit_tu_id')

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