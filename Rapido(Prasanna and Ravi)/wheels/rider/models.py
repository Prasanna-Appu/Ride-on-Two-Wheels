from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.

GENDER = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE')
)

STATE = (
    ('KARNATAKA','KARNATAKA')
)

CITY = (
    ('Gadag','Gadag'),
    ('Hubli-Dharwad','Hubli-Dharwad'),
    ('Belagavi','Belagavi'),
    ('Haveri','Haveri'),
    ('Mysore','Mysore'),
    ('Bengalore','Bengalore'),
    ('Mandya','Mandya'),
    ('Hassan','Hassan'),
)
class BookARide(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    city = models.CharField(max_length=20, choices=CITY)
    pick_up = RichTextField()
    drop_addr = RichTextField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email

class Emergency(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(max_length=20)
    
    gender = models.CharField(max_length=6, choices=GENDER)
    city = models.CharField(max_length=20, choices=CITY)
    state = models.CharField(max_length=20)
    pick_up = RichTextField()
    drop_addr = RichTextField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email

class RentingService(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    city = models.CharField(max_length=20, choices=CITY)
    Occupation = models.CharField(max_length=40,null=True, blank=True)
    curr_address = RichTextField()
    perm_address = RichTextField()
    driving_lic_no = models.CharField(max_length=30)
    rent_hrs = models.IntegerField(null=True,blank=True)
    rent_chars = models.IntegerField(null=True,blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email

class Careers(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    aadhar = models.IntegerField()
    email = models.EmailField(max_length=20)
    phoneno = models.IntegerField(null=True, blank=True)
    caddress = RichTextField()
    paddress = RichTextField()
    gender = models.CharField(max_length=6, choices=GENDER)
    dlno = models.CharField(max_length=30)
    rcno = models.CharField(max_length=30)
    is_bike_active = models.BooleanField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email