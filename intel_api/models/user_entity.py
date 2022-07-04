from django.db import models

from rpc_client_app.calls import fetch_user_profile, fetch_user_lab

class UserEntity(models.Model):
    user_profile_id = models.CharField(max_length=30,)
    username = models.CharField(max_length=200,)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_profile_id', 'username'], name='unique user entity')
        ]

    def user_profile(self):
        return fetch_user_profile(self.username)

    def get_lab(self):
        if self.user_profile() and self.user_profile().is_lab_user:
            return fetch_user_lab(int(self.user_profile_id))

    def get_lab_external_entity(self):
        from booking_manager_api.models.util import get_object_or_none
        from intel_api.models import ExternalEntity
        lab = self.get_lab()
        if lab:
            return get_object_or_none(ExternalEntity,entity_id=lab.id,entity_reg=lab.registration_number,entity_type=ExternalEntity.LAB)
        else:
            return None