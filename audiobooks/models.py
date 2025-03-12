from django.db import models
from base.models import Customer, Book,Purchase

class Audio_books(Book):
    audio_file = models.FileField(upload_to="audiobooks/")




