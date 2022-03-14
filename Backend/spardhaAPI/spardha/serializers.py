from rest_framework import serializers
from .models import Sport


class SportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sport
        fields = ['name', 'hostels', 'final_points']