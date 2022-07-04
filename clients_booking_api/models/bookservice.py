from django.db import models, IntegrityError
from datetime import datetime, timedelta
import datetime

from booking_manager_api.models import EntityWorkingDays, TimeSlot, EntityService, EntityBookingSchedule
from booking_manager_api.models.base_model import BaseModel
from booking_manager_api.utils.gen_code_util import gen_booking_code
from intel_api.models import UserEntity
from booking_manager_api.models.util import get_object_or_none

class UserBookService(BaseModel):
    booked_by =  models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    booked_entity_service = models.ForeignKey(EntityService, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    entity_booking_schedule = models.ForeignKey(EntityBookingSchedule, on_delete=models.CASCADE)
    code = models.CharField(max_length=30)
    payed = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['code'], name='unique code')
        ]

    @classmethod
    def create(cls,entity_service,date,booking_schedule,booked_by):
        obj = get_object_or_none(cls,booked_entity_service=entity_service,schedule_date=date,entity_booking_schedule=booking_schedule,booked_by=booked_by)
        if not obj:
            userbookservice = None
            while(userbookservice is None):
                try:
                    userbookservice = cls.objects.create(booked_entity_service=entity_service, schedule_date=date,
                                       entity_booking_schedule=booking_schedule, booked_by=booked_by,code=gen_booking_code())
                except IntegrityError as e:
                    userbookservice = cls.objects.create(booked_entity_service=entity_service, schedule_date=date,
                                                         entity_booking_schedule=booking_schedule, booked_by=booked_by,code=gen_booking_code())

            return userbookservice
        # return obj
        return None

    @classmethod
    def get_external_entity_bookings(cls,external_entity):
        entity_service = EntityService.get_entity_services(external_entity)
        return cls.objects.filter(booked_entity_service__in=entity_service)

    @classmethod
    def get_patient_bookings(cls,user_entity):
        return cls.objects.filter(booked_by=user_entity).select_related("booked_entity_service","entity_booking_schedule")

    @classmethod
    def get_user_book_service_by_code(cls,code):
        return get_object_or_none(cls,code=code)

    def is_sharing_enabled(self):
        return True if self.booked_entity_service.sharing_consent_required else False

    # def get_external_entity_country(self):
    #     external_entity = self.booked_entity_service.get_external_entity()
    #     return external_entity['country']




