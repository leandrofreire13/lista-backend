from django.shortcuts import render
from rest_framework import viewsets

from .models import ShoppingItem
from .serializers import ShoppingItemSerializer


# As views funcionam como uma controller para orientar o que será feito.

class ShoppingItemViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()
