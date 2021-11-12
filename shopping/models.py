from django.db import models


# Modelo de cadastro da lista de compra.

class ShoppingItem(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.PositiveSmallIntegerField()
    checked = models.BooleanField(default=False)
