from django.db import models
from base.models import Book
from accountmanage.models import Purchase, Customer
class Education_books(Book):
    file = models.FileField(upload_to="education/")


