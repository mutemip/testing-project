from django.db import models

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    interval_in_minute = models.IntegerField(default=60)

    @classmethod
    def get_slots_by_interval(cls,interval):
        return cls.objects.filter(interval_in_minute=interval)