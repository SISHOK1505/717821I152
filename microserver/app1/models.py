from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField()
    roll_number = models.CharField(max_length=10)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
