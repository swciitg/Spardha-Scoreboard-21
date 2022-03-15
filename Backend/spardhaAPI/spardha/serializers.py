from rest_framework import serializers
from .models import Hostel, Point, Match

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

class MatchSerializer(serializers.ModelSerializer):
    team1 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    team2 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')
    status = serializers.SlugRelatedField(read_only=True,slug_field='status')

    class Meta:
        model = Match
        fields = ['team1','team2','sport','date_time','status','stage']

        
        