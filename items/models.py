from django.db import models


class ItemList(models.Model):
    price = models.CharField(max_length=200)
    postal = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    shopNick = models.CharField(max_length=200)
    payNum = models.CharField(max_length=200)
    count = models.PositiveIntegerField()
    image = models.CharField(max_length=200)
