from django.db import models
import datetime

# Create your models here.
class Record(models.Model):
	staff_num  = models.PositiveIntegerField(default=0)
	staff_name = models.CharField(max_length=100)
	
class Detail(models.Model):
	record     = models.ForeignKey(Record, on_delete=models.CASCADE)
	work_date  = models.CharField(max_length=100)
	work_day   = models.CharField(max_length=100)
	entry_time = models.CharField(max_length=100,null=True)
	exit_time  = models.CharField(max_length=100,null=True)
	remark     = models.CharField(max_length=100,blank=True)
	reason     = models.CharField(max_length=50,blank=True,null=True)

class Holiday(models.Model):
	holiday_type = models.CharField(max_length=40,null=True,blank=True)
	date         = models.CharField(max_length=100)