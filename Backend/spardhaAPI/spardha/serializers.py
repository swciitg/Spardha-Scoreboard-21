from rest_framework import serializers
from .models import Hostel, Point


class HostelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hostel
        fields = ['name', 'overall_points']

class StandingSerializer(serializers.ModelSerializer):
    hostel = serializers.SlugRelatedField(read_only=True,slug_field='name')
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')

    class Meta:
        model = Point
        fields = ['hostel', 'sport', 'points']

        
        