from django.db import models
from base.models import Book, Customer, Purchase

class ebooks(Book):
    file = models.FileField(upload_to="ebooks/")

    
