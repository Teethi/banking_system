from django.db import models

# Create your models here.

class BankUser(models.Model):
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
    has_account=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(BankUser, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def _str_(self):
        return self.account_number