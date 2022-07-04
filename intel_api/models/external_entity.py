from django.db import models
from rpc_client_app.calls import retrieve_lab


class ExternalEntity(models.Model):
    LAB = "Lab"

    entity_type_option = (
        (LAB, LAB),
    )

    entity_id = models.CharField(max_length=30,)
    entity_reg = models.CharField(max_length=200,null=True)
    entity_type = models.CharField(max_length=200,null=True,choices=entity_type_option)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entity_id', 'entity_type'], name='unique entity')
        ]

    @property
    def detail(self):
        if self.entity_type == self.LAB:
            return retrieve_lab(int(self.entity_id))

    @classmethod
    def create(cls,entity_id,entity_reg,entity_type):
        return cls.objects.create(entity_id=entity_id,entity_reg=entity_reg,entity_type=entity_type)

