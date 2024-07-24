from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'codigo', 'nombre', 'alias', 'estado', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'validators': []},  # Remove default validators if not needed
            'alias': {'required': False}, 
        }