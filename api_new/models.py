from django.db import models


# Create your models here.
class Moto(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    concern = models.ManyToManyField('Concern')

    def __str__(self):
        return self.brand


class Store(models.Model):
    title = models.CharField(max_length=255)
    concern = models.ForeignKey('Concern', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Concern(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Aero(models.Model):
    city = models.CharField(max_length=55)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Avia(models.Model):
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    price = models.IntegerField()
    aeroport = models.ManyToManyField('Aero')

    def __str__(self):
        return self.brand


