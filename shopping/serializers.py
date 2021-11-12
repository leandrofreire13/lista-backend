from rest_framework import serializers

# Importar o model
from .models import ShoppingItem

# O Serializer é responsável por transformar os dados de objeto para Json


class ShoppingItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingItem
        fields = '__all__'
