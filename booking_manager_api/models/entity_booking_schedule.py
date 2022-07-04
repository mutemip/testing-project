
from django.db import models
from datetime import datetime, timedelta
import datetime

from booking_manager_api.models import EntityWorkingDays, TimeSlot
from booking_manager_api.models.base_model import BaseModel
from intel_api.models import UserEntity



class EntityBookingSchedule(BaseModel):
    entity_working_days = models.ForeignKey(EntityWorkingDays, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserEntity,related_name="entity_booking_sched_creator", on_delete=models.CASCADE)
    maximum_bookee = models.IntegerField(default=200)
    active = models.BooleanField(default=True)

    @classmethod
    def create(cls,entity_working_days,timeslot,created_by,maximum_bookee):
        return cls.objects.create(entity_working_days=entity_working_days,timeslot=timeslot,created_by=created_by,maximum_bookee=maximum_bookee)

    @classmethod
    def get_active_schedules(cls,day,entity_service,date):
        from clients_booking_api.models import UserBookService
        data = list()
        schedules = cls.objects.filter(entity_working_days=day,active=True).select_related('timeslot')
        for schedule in schedules:
            booked_users = UserBookService.objects.filter(booked_entity_service=entity_service,schedule_date=date,entity_booking_schedule=schedule).count()
            if not booked_users >= schedule.maximum_bookee:
                data.append(schedule)
        return data

    @classmethod
    def entity_booking_schedules(cls,external_entity):
        return cls.objects.filter(entity_working_days__bookable_entity=external_entity)
