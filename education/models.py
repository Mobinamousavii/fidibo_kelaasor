from django.db import models
from base.models import Book, Customer, Purchase
class Education_books(Book):
    file = models.FileField(upload_to="education/")


