from django.db import models
from base.models import Book

class fidiplus_book(Book):
    file = models.FileField(upload_to="fidiplus_book/")
