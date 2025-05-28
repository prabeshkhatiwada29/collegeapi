from django.db import models

# Create your models here.
# create a college model

class College(models.Model):
    name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established_year = models.IntegerField()
    courses_offered = models.TextField()  # Store as a comma-separated string or JSON
  
# create a student model
