from django.db import models

# Create your models here.

class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
