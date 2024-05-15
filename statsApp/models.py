from django.db import models
from mainApp.models import *
from userApp.models import *

class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.FloatField()
    summa = models.FloatField()
    tolandi = models.FloatField(default=0)
    qarz = models.FloatField(default=0, validators=MinValueValidator[0])
    sana = models.DateTimeField(auto_now_add=True)
    tarqatuvchi = models.ForeignKey(Tarqatuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mahsulot.nom} - {self.mijoz.ism}"
