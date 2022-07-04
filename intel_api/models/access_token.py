import binascii
import os

from django.db import models

from booking_manager_api.models.base_model import BaseModel
from intel_api.models import UserEntity


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()

class AccessToken(BaseModel):
    user_entity =  models.ForeignKey(UserEntity, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=200,)
    token = models.CharField(max_length=200,)
    is_login = models.BooleanField(default=True)

    @classmethod
    def create(cls,user_entity,session_key):
        return cls.objects.create(user_entity=user_entity,session_key=session_key,token=generate_key())

    def is_lab_user(self):
        return True if self.user_entity.user_profile().is_lab_user else False

    def get_external_entity(self):
        lab_user = self.is_lab_user()
        if lab_user:
            return self.user_entity.get_lab_external_entity()
        else:
            raise Exception("Cannot get lab of none lab user.")