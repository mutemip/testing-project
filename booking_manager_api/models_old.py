# from django.db import models
# from django.core.exceptions import ValidationError
# from django.contrib.postgres.fields import ArrayField
# from datetime import datetime, timedelta
# import datetime
#
#
# SLOT_CHOICES = (
#     ('Slot 1', 'S1'),
#     ('Slot 2', 'S2'),
#     ('Slot 3', 'S3'),
#     ('Slot 4', 'S4'),
# )
#
#
#
#
#
# class DateAndSlot(models.Model):
#     booking_date = models.DateField(blank=False)
#     booking_slot = models.TextField(choices=SLOT_CHOICES, blank=False)
#     labs_added = models.BooleanField(default=False)
#
#     class Meta:
#         unique_together = ('booking_date', 'booking_slot')
#
#     def save(self, *args, **kwargs):
#         if self.booking_date < datetime.date.today():
#             raise ValidationError("date must be in future")
#         super(DateAndSlot, self).save(*args, **kwargs)
#
#     def handle(self, *args, **options):
#         DateAndSlot.objects.filter(self.booking_date - timedelta(days=1)).delete()
#         self.stdout.write('Deleted objects older than 10 days') #Can be changed or removed
#
#     def __str__(self):
#         return ("Date : {0} \n Slot: {1}" .format(self.booking_date, self.booking_slot))
#
#
# class AvailableLabs(models.Model):
#     """Model for declaring labs for particular time slot"""
#
#     booking_date_slot = models.OneToOneField(
#         DateAndSlot, on_delete=models.CASCADE, blank=False, unique=True)
#     booking_times = ArrayField(models.CharField(max_length=200), blank=False) #Time available per slot e.g [12:00 12:30,12:30 13:00,13:05 14:00]
#     labs_available = models.IntegerField(null=True) #Number of reservations available per slot
#
#     def __str__(self):
#         return ("Booking Date : {0} \n Booking Slot: {1} \n Available Labs: {2} " .format(self.booking_date_slot.booking_date, self.booking_date_slot.booking_slot, self.labs_available))
#
#
# class Lab(models.Model):
#     """Model for generating labs object for particular slot"""
#     chosen_date_slot = models.ForeignKey(DateAndSlot, on_delete=models.CASCADE)
#     lab_name = models.CharField(max_length=200, blank=False)
#     is_booked = models.BooleanField(default=False)
#
#     def __str__(self):
#         return ("Lab name : {} => {}".format(self.lab_name, self.chosen_date_slot))
