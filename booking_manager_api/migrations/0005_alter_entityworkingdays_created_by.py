# Generated by Django 3.2 on 2021-09-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intel_api', '0006_alter_accesstoken_token'),
        ('booking_manager_api', '0004_entityservice_sharing_consent_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entityworkingdays',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_working_days_creator', to='intel_api.userentity'),
        ),
    ]
