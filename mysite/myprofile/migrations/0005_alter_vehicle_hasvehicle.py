# Generated by Django 4.0.1 on 2022-03-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0004_vehicle_hasvehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='hasVehicle',
            field=models.BooleanField(default=True),
        ),
    ]
