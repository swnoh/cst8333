from django.db import models


class Dataset (models.Model):
    ref_date = models.CharField(max_length=100, default=" ")
    geo = models.CharField(max_length=100, default=" ")
    est = models.CharField(max_length=100, default=" ")
    vector = models.CharField(max_length=100, default=" ")
    coordinate = models.CharField(max_length=100, default=" ")
    value = models.CharField(max_length=100, default=0)


    def __str__(self):
        return self.geo
