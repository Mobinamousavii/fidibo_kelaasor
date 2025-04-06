from django.db import models
from base.models import  Book
from accountmanage.models import Purchase, Customer

class Audio_books(Book):
    audio_file = models.FileField(upload_to="audiobooks/")




