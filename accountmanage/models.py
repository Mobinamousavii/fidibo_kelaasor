from django.db import models
from base.models import  Book

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    payment = models.BooleanField(default=False)
    password = models.CharField(max_length=20)

class Purchase(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="purchased_customer")
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="purchased_book")
