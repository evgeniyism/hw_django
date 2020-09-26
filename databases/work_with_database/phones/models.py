from django.db import models
from datetime import date

class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

