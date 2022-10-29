from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class HomeCurosol(models.Model):
    photo = models.ImageField(upload_to ='media/home/cursol/%Y/')
    head = models.CharField(max_length=60)
    subhead = RichTextField()
    def __str__(self):
        return self.head 

    

class HomeJumbotron(models.Model):
    head = models.CharField(max_length=60)
    subhead = RichTextField()

class HomeCard(models.Model):
    photo = models.ImageField(upload_to ='media/home/cards/%Y/')
    city = models.CharField(max_length=60)
    desc = RichTextField()
    rto_no = models.CharField(max_length=25)
    def __str__(self):
        return self.city


class AboutJumbo(models.Model):
    head = models.CharField(max_length=60)
    subhead = RichTextField()

class AboutJumbo2(models.Model):
    head = models.CharField(max_length=60)
    subhead = RichTextField()

class AboutJumbo3(models.Model):
    head = models.CharField(max_length=60)
    subhead = RichTextField()

class Services(models.Model):
   
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField()
    address = RichTextField()
    message = models.TextField(blank=True)

    
    def __str__(self):
        return self.name









