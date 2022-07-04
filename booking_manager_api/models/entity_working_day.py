from django.db import models

from datetime import datetime, timedelta
import datetime

from booking_manager_api.models import DaysOfTheWeek
from booking_manager_api.models.base_model import BaseModel
from intel_api.models import ExternalEntity, UserEntity


class EntityWorkingDays(BaseModel):
    bookable_entity = models.ForeignKey(ExternalEntity, on_delete=models.CASCADE)
    day = models.ForeignKey(DaysOfTheWeek, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserEntity,related_name="entity_working_days_creator", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    @classmethod
    def create(cls,entity,day,created_by):
        return cls.objects.create(bookable_entity=entity,day=day,created_by=created_by)

    @classmethod
    def get_entity_bookings(cls,entity):
        return cls.objects.filter(bookable_entity=entity).select_related('bookable_entity','created_by','day')

    