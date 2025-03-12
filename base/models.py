from django.db import models
from ebooks.models import Ebooks
from audiobooks.models import Audio_books
from magazines.models import Magazines


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    rate = models.IntegerField()
    price = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    payment = models.BooleanField(default=False)

class Purchase(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="purchased_customer")
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="purchased_book")

