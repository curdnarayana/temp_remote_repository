from django.db import models
from multiselectfield import MultiSelectField

class MatrimonyData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    sal = models.IntegerField()
    mobile = models.BigIntegerField(unique=True)
    color = models.CharField(max_length=30)
    weight = models.IntegerField()
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20,unique=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    height = models.FloatField()

    GENDER_CHOICES=(
        ('F','Female'),
        ('M','Male')
    )
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES)

    LOCATION_CHOICES=(
        ('Hyd','Hyderabad'),
        ('Bang','Bangalore'),
        ('Chen','Chennai'),
        ('Mum','Mumbai')
    )
    locations = MultiSelectField(max_length=20, choices=LOCATION_CHOICES)

    JOB_CHOICES=(
        ('Govt','Govt Job'),
        ('S/W','Software'),
        ('Trainers','Teachers'),
        ('Doctor','Doctors'),
        ('Police','Police')
    )
    jobtype = MultiSelectField(max_length=20, choices=JOB_CHOICES)

    LOOKING_CHOICES=(
        ('Male','GROOM'),
        ('Female','BRIDE')
    )
    looking_for = models.CharField(max_length=20,choices=LOOKING_CHOICES)

    address = models.CharField(max_length=100)