from django.db import models
from base.models import Book
class Magazines(Book):
    file = models.FileField(upload_to="magazines/")
