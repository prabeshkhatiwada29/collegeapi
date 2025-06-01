from django.db import models


# Create your models here.
# create a college model

class College(models.Model):
    name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established_year = models.IntegerField()
    courses_offered = models.TextField() 
    
    def __str__(self):
        return self.name + self.location  # Return a string representation of the college
     # Store as a comma-separated string or JSON
  
# create a student model
class student(models.Model):
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='students')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    enrollment_date = models.DateField(auto_now_add=True)
    graduation_date = models.DateField(null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)

   

class staff(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='staff')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    hire_date = models.DateField(auto_now_add=True)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)



  # Return a string representation of the staff member
