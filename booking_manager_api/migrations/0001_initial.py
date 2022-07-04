# Generated by Django 3.2 on 2021-09-08 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intel_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaysOfTheWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('interval_in_minute', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='EntityWorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('bookable_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intel_api.externalentity')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager_api.daysoftheweek')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntityBookingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField()),
                ('maximum_bookee', models.IntegerField(default=200)),
                ('active', models.BooleanField(default=True)),
                ('entity_working_days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager_api.entityworkingdays')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager_api.timeslot')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
