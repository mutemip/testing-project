# Generated by Django 3.2 on 2021-09-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_id', models.CharField(max_length=30)),
                ('entity_reg', models.CharField(max_length=200, null=True)),
                ('entity_type', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
