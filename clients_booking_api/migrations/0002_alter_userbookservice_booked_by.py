# Generated by Django 3.2 on 2021-09-22 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients_booking_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookservice',
            name='booked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
