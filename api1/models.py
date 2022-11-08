from django.db import models


class Category(models.Model):
    title = models.CharField('Категория', max_length=500)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField('Название', max_length=500)
    slug = models.SlugField(unique=True)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    salons = models.ManyToManyField('Salon')

    def __str__(self):
        return self.title


class Salon(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=55)
    age = models.IntegerField()
    rete = models.DecimalField(max_digits=8, decimal_places=2)
    house = models.ForeignKey('Houses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Houses(models.Model):
    adres = models.CharField(max_length=255)

    def __str__(self):
        return self.adres


class Cities(models.Model):
    name = models.CharField(max_length=55)
    adres = models.ManyToManyField("Houses")
