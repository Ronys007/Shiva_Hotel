from django.db import models

# Create your models here.
class Booking(models.Model):
    firstname= models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    address= models.CharField(max_length=255, blank=False)
    number=models.IntegerField(blank=False)
    adhaarcard=models.IntegerField(blank=False)
    hotel_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.firstname
