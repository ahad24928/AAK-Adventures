from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='countries/', null=True, blank=True)  
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name

class Treking(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField() 
    events = models.TextField(null=True, blank=True)   
    image = models.ImageField(upload_to='treking/', null=True, blank=True)
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Camping(models.Model):
    namecamp = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    about = models.TextField()  
    image = models.ImageField(upload_to='camping/', null=True, blank=True)

    def __str__(self):
        return self.namecamp

class Caravan(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField() 
    amenties = models.TextField(null=True, blank=True)   
    image = models.ImageField(upload_to='caravan/', null=True, blank=True)
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    TYPE_CHOICES = (
        ('treking', 'Treking'),
        ('camping', 'Camping'),
        ('caravan', 'Caravan'),
    )
    
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    phone = models.CharField(max_length=15)

    booking_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    item_id = models.IntegerField()

    check_in = models.DateField()
    check_out = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_name} - {self.booking_type}"