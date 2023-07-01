from django.db import models

# Create your models here.

class User(models.Model):
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

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return f"{self.account_number} {self.balance}"
    
