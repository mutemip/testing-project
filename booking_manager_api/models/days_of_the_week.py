from django.db import models
from datetime import datetime, timedelta
import datetime


class DaysOfTheWeek(models.Model):
    day = models.CharField(max_length=30,)

    @classmethod
    def get_days(cls):
        return cls.objects.all()
    
    @classmethod
    def days_as_list(cls):
        return cls.get_days().values_list('id','day')
    