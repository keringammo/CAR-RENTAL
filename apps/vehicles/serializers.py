from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'owner', 'brand', 'model', 'year', 'price_per_day', 'is_available', 'image']
