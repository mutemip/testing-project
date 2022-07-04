from django.db import models, IntegrityError

from booking_manager_api.models.base_model import BaseModel

from clients_booking_api.models import UserBookService


class UserBookTravelInformation(BaseModel):
    userbookservice = models.ForeignKey(UserBookService, on_delete=models.CASCADE)
    travel_date = models.DateTimeField(null=True)
    departure_country = models.CharField(max_length=100,null=True)
    arrival_country = models.CharField(max_length=100,null=True)
    passport_number = models.CharField(max_length=100,null=True)
    transport_operator = models.CharField(max_length=100,null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userbookservice'], name='unique booking')
        ]


    @classmethod
    def create(cls,userbookservice,travel_date,departure_country,arrival_country,passport_number,transport_operator):
        return cls.objects.create(
                userbookservice=userbookservice,
                travel_date=travel_date,
                departure_country=departure_country,
                arrival_country=arrival_country,
                passport_number=passport_number,
                transport_operator=transport_operator
            )