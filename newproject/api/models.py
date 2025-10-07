
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # e.g. 8.5

    def _str_(self):
        return self.title

