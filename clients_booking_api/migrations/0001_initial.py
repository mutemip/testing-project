# Generated by Django 3.2 on 2021-09-10 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking_manager_api', '0002_bookableservice_entityservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booked_by', models.IntegerField()),
                ('schedule_date', models.DateField()),
                ('code', models.CharField(max_length=30)),
                ('payed', models.BooleanField(default=False)),
                ('booked_entity_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager_api.entityservice')),
                ('entity_booking_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager_api.entitybookingschedule')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
