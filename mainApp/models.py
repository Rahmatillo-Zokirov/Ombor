from django.core.validators import MinValueValidator
from django.db import models
from userApp.models import *


class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    dokon = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=14)
    manzil = models.TextField()
    qarz = models.FloatField(default=0, validators=[MinValueValidator(0)])
    tarqatuvchi = models.ForeignKey(Tarqatuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Mahsulot(models.Model):
    nom = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    narx1 = models.FloatField()
    narx2 = models.FloatField(blank=True, null=True)
    miqdor = models.FloatField()
    olchov = models.CharField(max_length=20)
    sana = models.DateField(auto_now=True)
    tarqatuvchi = models.ForeignKey(Tarqatuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

