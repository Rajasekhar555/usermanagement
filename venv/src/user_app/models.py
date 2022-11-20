from django.db import models

class UserData(models.Model):
    username             = models.CharField(max_length=100)
    password             = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender               = models.CharField(max_length=1, choices=GENDER_CHOICES)
    experience           = models.IntegerField(default=0)
    date_of_joining      = models.DateField(max_length=100)
    designation          = models.CharField(max_length=100)
    active               = models.BooleanField(default=True)
