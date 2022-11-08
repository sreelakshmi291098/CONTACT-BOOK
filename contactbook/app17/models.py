from django.db import models

# Create your models here.


class Contact(models.Model):
    # Id=models.IntegerField(unique=True)
    Firstname=models.CharField(max_length=30)
    Phonenumber=models.IntegerField(unique=True)