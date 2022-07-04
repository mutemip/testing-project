from django.db import models
from booking_manager_api.models.base_model import BaseModel
from intel_api.models import ExternalEntity
import moneyed
from djmoney.models.fields import MoneyField

from rpc_client_app.calls import retrieve_labtest, all_tests


class BookableService(BaseModel):
    TEST = "Test"

    bookable_service_type = (
        (TEST,TEST),
    )

    service_id = models.IntegerField()
    service_type = models.CharField(max_length=60,choices=bookable_service_type)

    def detail(self):
        if self.service_type == self.TEST:
            return retrieve_labtest(self.service_id)


    @classmethod
    def load_test_service(cls):
        tests = all_tests()
        if tests:
            for labtest in tests:
                cls.objects.update_or_create(service_id=labtest, service_type=BookableService.TEST,
                                                         defaults={"service_id": labtest,
                                                                   "service_type": BookableService.TEST})


    @classmethod
    def load_bookable_service(cls):
        cls.load_test_service()





class EntityService(BaseModel):
    service_name = models.CharField(max_length=150,null=True)
    bookable_entity = models.ForeignKey(ExternalEntity, on_delete=models.CASCADE)
    service = models.ForeignKey(BookableService, on_delete=models.CASCADE)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    payment_required = models.BooleanField(default=False)
    sharing_consent_required = models.BooleanField(default=False)

    @classmethod
    def create(cls,bookable_entity,service,price,payment_required,sharing_consent_required,service_name):
        # obj = cls.objects.filter(bookable_entity=bookable_entity,service_name=service_name)
        # if obj.exists():
        #     return Exception("A service with the service name({}) exists.".format(service_name))
        return cls.objects.create(bookable_entity=bookable_entity,service=service,price=price,payment_required=payment_required,
                                    sharing_consent_required=sharing_consent_required,service_name=service_name)

    @classmethod
    def get_entity_services(cls,external_entity):
        return cls.objects.filter(bookable_entity=external_entity).select_related('service')


    @classmethod
    def get_external_entity(cls):
        return cls.bookable_entity.detail
