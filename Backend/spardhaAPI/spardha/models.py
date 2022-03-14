from email.policy import default
from statistics import mode
from django.db import models
from django.db.models.base import Model
# Create your models here.

from django.contrib.postgres.fields import ArrayField

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    overall_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Format(models.Model):
    format = models.CharField(max_length=100)

    def __str__(self):
        return self.format

class Sport(models.Model):
    name = models.CharField(max_length=100)
    hostels = models.ManyToManyField("Hostel",null= True)
    format = models.ForeignKey("Format",  on_delete=models.CASCADE,null= True)
    final_points = models.IntegerField()
    # logo = models.ImageField(default="default.jpg", upload_to="logos")

    def __str__(self):
        return self.name

class Sport_League(models.Model):
    hostels = models.ForeignKey("Hostel",  on_delete=models.CASCADE,null= True)
    format = models.ForeignKey("Format",  on_delete=models.CASCADE,null= True)
    standings = ArrayField(models.IntegerField(), default=list)
    final_points = models.IntegerField()

    def __str__(self):
        return self.name

class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Stage(models.Model):
    stage = models.CharField(max_length=100)

    def __str__(self):
        return self.stage

class Match(models.Model):
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE,null= True)
    date_time = models.DateTimeField(auto_now_add=True)
    team1 = models.ForeignKey("Hostel", related_name="team1", on_delete=models.CASCADE,null= True)
    team2 = models.ForeignKey("Hostel", related_name="team2", on_delete=models.CASCADE,null= True)
    stage = models.ForeignKey("Stage",  on_delete=models.CASCADE,null= True)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    points1 = models.IntegerField()
    points2 = models.IntegerField()

    def __str__(self):
        return self.sport

class Match_all(models.Model):
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.ForeignKey("Status",  on_delete=models.CASCADE,null= True)
    date_time = models.DateTimeField(auto_now_add=True)
    round = models.ForeignKey("Stage",  on_delete=models.CASCADE,null= True)
    scores = ArrayField(models.IntegerField(), default=list)
    points_awarded = ArrayField(models.IntegerField(), default=list)

    def __str__(self):
        return self.sport