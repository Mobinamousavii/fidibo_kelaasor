from django.db import models
from base.models import Book, Customer, Purchase

class Ebooks(Book):
    file = models.FileField(upload_to="ebooks/")

    
