from django.db import models

# Create your models here.

class Schools(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    no_of_students = models.IntegerField()

    def __str__(self):
        return self.name
