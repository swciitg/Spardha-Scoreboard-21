from rest_framework import serializers
from .models import *

class HostelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hostel
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'

class StandingSerializer(serializers.ModelSerializer):
    hostel = serializers.SlugRelatedField(read_only=True,slug_field='name')
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')

    class Meta:
        model = Point
        fields = ['hostel', 'sport', 'points']

class MatchASerializer(serializers.ModelSerializer):
    team1 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    team2 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')

    class Meta:
        model = MatchA
        fields = ['team1','team2','sport','date','time','status','score1','score2','stage','winner']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ["id","match"]
class MatchBSerializer(serializers.ModelSerializer):
    team1 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    team2 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')
    scores = GameSerializer(source = "game_set",many = True)
    class Meta:
        model = MatchB
        fields = ['team1','team2','sport','date','time','status','stage','scores','winner']

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        exclude = ["id","match"]
class MatchCSerializer(serializers.ModelSerializer):
    team1 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    team2 = serializers.SlugRelatedField(read_only=True,slug_field='name')
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')
    # sets = SetSerializer(many = True, source="set_set")
    class Meta:
        model = MatchC
        fields = ['team1','team2','sport','date','time','status','stage','winner']


class ScoreSerializer(serializers.ModelSerializer):
    hostel = serializers.SlugRelatedField(read_only=True,slug_field='name')
    class Meta:
        model = Score
        fields = ['hostel','score']

class MatchDSerializer(serializers.ModelSerializer):
    sport = serializers.SlugRelatedField(read_only=True,slug_field='name')
    round = serializers.SlugRelatedField(read_only=True,slug_field='stage')
    scores = ScoreSerializer(source = "score_set",many = True)
    class Meta:
        model = MatchD
        fields = ['name','sport','date','time','status','round','scores']

        
