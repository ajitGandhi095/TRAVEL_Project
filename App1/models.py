from django.db import models

# Create your models here.
class UserInfo(models.Model):
    Fname= models.CharField(max_length=30)
    Lname= models.CharField(max_length=30, primary_key=True)
    gmail= models.CharField(max_length=50)
    password= models.CharField(max_length=30)
    mobile= models.BigIntegerField()