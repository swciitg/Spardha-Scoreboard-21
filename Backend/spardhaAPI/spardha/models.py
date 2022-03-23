from pydoc import classname
from pyexpat import model
from random import choices
from re import S
import re
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Hostel(models.Model):
    CHOICES = ((1,'Boys'),(2,'Girls'))
    name = models.CharField(max_length=100)
    overall_points = models.IntegerField(default=0)
    type = models.IntegerField(choices=CHOICES,null=True)

    def __str__(self):
        return self.name

# class Format(models.Model):
#     format = models.CharField(max_length=10,
#     help_text="A - Football, Hockey, Cricket, Khokho, Basketball, Water Polo.  B - Lawn Tennis, Volleyball. C - Badminton, Table Tennis, Squash. D - Rest everything")

#     def __str__(self):
#         return self.format

class Sport(models.Model):
    FORMATS = ((1,'A'),(2,'B'),(3,'C'),(4,'D'))
    name = models.CharField(max_length=100,null=True)
    # hostels = models.ManyToManyField("Hostel")
    format = models.IntegerField(choices=FORMATS,help_text="A - Football, Hockey, Cricket, Khokho, Basketball, Water Polo.  B - Lawn Tennis, Volleyball. C - Badminton, Table Tennis, Squash. D - Rest everything")

    def __str__(self):
        return self.name

class Stage(models.Model):
    stage = models.CharField(max_length=100)

    def __str__(self):
        return self.stage

class Point(models.Model):
    hostel = models.ForeignKey("Hostel", related_name="hostels", on_delete=models.CASCADE,null= True)
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    points = models.IntegerField()

    class Meta:
        unique_together = ('hostel', 'sport',)

    def __str__(self):
        return self.sport.name+" ( "+self.hostel.name+" ) "

    def save(self, *args, **kwargs):
        super(Point, self).save(*args, **kwargs)
        total_score = 0
        for point in Point.objects.all().filter(hostel=self.hostel):
            total_score = total_score + point.points
        self.hostel.overall_points = total_score
        self.hostel.save()

class MatchA(models.Model):
    TEAMS = ((1,'team1'),(2,'team2'))
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.BooleanField(default= False,help_text="Enter 0 for upcoming and 1 for completed") 
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    team1 = models.ForeignKey("Hostel", related_name="team1", on_delete=models.CASCADE,null= True)
    team2 = models.ForeignKey("Hostel", related_name="team2", on_delete=models.CASCADE,null= True)
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE,null= True)
    score1 = models.CharField(max_length=15,null=True,blank=True)
    score2 = models.CharField(max_length=15,null=True,blank=True)
    winner = models.IntegerField(choices=TEAMS,null=True,blank=True)
    @property
    def name(self):
        return self.team1.name+" vs "+self.team2.name

class MatchB(models.Model):
    TEAMS = ((1,'team1'),(2,'team2'))
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.BooleanField(default= False,help_text="Enter 0 for upcoming and 1 for completed") 
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    team1 = models.ForeignKey("Hostel", related_name="player1", on_delete=models.CASCADE,null= True)
    team2 = models.ForeignKey("Hostel", related_name="player2", on_delete=models.CASCADE,null= True)
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE,null= True)
    winner = models.IntegerField(choices=TEAMS,null=True,blank=True)

    def __str__(self):
        return self.team1.name+" vs "+self.team2.name

class MatchC(models.Model):
    TEAMS = ((1,'team1'),(2,'team2'))
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.BooleanField(default= False,help_text="Enter 0 for upcoming and 1 for completed") 
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    team1 = models.ForeignKey("Hostel", related_name="p1", on_delete=models.CASCADE,null= True)
    team2 = models.ForeignKey("Hostel", related_name="p2", on_delete=models.CASCADE,null= True)
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE,null= True)
    winner = models.IntegerField(choices=TEAMS,null=True,blank=True)

    def __str__(self):
        return self.team1.name+" vs "+self.team2.name

class MatchD(models.Model):
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    hostels = models.ManyToManyField("Hostel")
    status = models.BooleanField(default= False,help_text="Enter 0 for upcoming and 1 for completed") 
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    round = models.ForeignKey("Stage",  on_delete=models.CASCADE,null= True)

    @property
    def name(self):
        return self.sport.name + " - " + self.round.stage
    def __str__(self):
        return self.sport.name + " - " + self.round.stage



class Score(models.Model):
    hostel = models.ForeignKey("Hostel", related_name="hostel", on_delete=models.CASCADE,null= True)
    match = models.ForeignKey("MatchD",  on_delete=models.CASCADE,null= True)
    score = models.IntegerField()

    class Meta:
        unique_together = ('hostel', 'match',)

    def __str__(self):
        return self.match.name+" ( "+self.hostel.name+" ) "

class Game(models.Model): # For match B
    score_team1 = models.CharField(max_length=15,null=True,blank=True)
    score_team2 = models.CharField(max_length=15,null=True,blank=True)
    match = models.ForeignKey("MatchB", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "game"

class Set(models.Model): # For match C
    name = models.CharField(max_length=11,null=True,blank=True)
    score_team1_game1 = models.CharField(max_length=15,null=True,blank=True)
    score_team2_game1 = models.CharField(max_length=15,null=True,blank=True)

    score_team1_game2 = models.CharField(max_length=15,null=True,blank=True)
    score_team2_game2 = models.CharField(max_length=15,null=True,blank=True)
   
    score_team1_game3 = models.CharField(max_length=15,null=True,blank=True)
    score_team2_game3 = models.CharField(max_length=15,null=True,blank=True)
    
    score_team1_game4 = models.CharField(max_length=15,null=True,blank=True)
    score_team2_game4 = models.CharField(max_length=15,null=True,blank=True)
   
    score_team1_game5 = models.CharField(max_length=15,null=True,blank=True)
    score_team2_game5 = models.CharField(max_length=15,null=True,blank=True)
    match = models.ForeignKey("MatchC", related_name="game", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "sets"
