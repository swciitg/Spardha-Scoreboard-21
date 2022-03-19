from rest_framework import serializers
from .models import *

class HostelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hostel
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    format = serializers.SlugRelatedField(read_only=True,slug_field='format')
    
    class Meta:
        model = Sport
        fields = '__all__'

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

    class Meta:
        model = Match
        fields = ['team1','team2','sport','date','time','status','score1','score2','stage']

class MatchAllSerializer(serializers.ModelSerializer):
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')
    round = serializers.SlugRelatedField(read_only=True,slug_field='stage')

    class Meta:
        model = Match_all
        fields = ['name','sport','hostels','date','time','status','round']
