from django.db import models

# Create your models here.
class Persons(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    age = models.IntegerField()


    def __str__(self):
        return self.name, self.surname


