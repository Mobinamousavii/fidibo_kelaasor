from django.db import models

class Magazines(models.Model):
    file = models.FileField(upload_to="magazines/")
