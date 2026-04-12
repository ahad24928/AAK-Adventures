from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Treking(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField()   # better than CharField
    image = models.ImageField(upload_to='trekking/', null=True, blank=True)

    def __str__(self):
        return self.name