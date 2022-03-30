from django.db import models

# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Location(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    firstAddress = models.CharField(max_length=200)
    secondAddress = models.CharField(max_length=200)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()

class Profession(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    companyName = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)

class Vehicle(models.Model):
    hasVehicle = models.BooleanField(default=True)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    VEHICLE_CHOICE = [('motorcycle','MOTOR CYCLE'),
    ('car','CAR'),
    ('truck','TRUCK'),]
    vehicleType = models.CharField(max_length=50,choices=VEHICLE_CHOICE,default='car')
    MAKE_CHOICE = [('nissan','NISSAN'),
    ('jeep','JEEP'),
    ('subaru','SUBARU'),]
    make = models.CharField(max_length=20,choices=MAKE_CHOICE,default='nissan')
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
