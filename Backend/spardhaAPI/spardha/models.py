from django.db import models
from django.db.models.base import Model

# Create your models here.

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
    name = models.CharField(max_length=100,null=True)
    hostels = models.ManyToManyField("Hostel")
    format = models.ForeignKey("Format",  on_delete=models.CASCADE,null= True)
    final_points = models.JSONField(default=dict,null=True,blank=True)
    # logo = models.ImageField(default="default.jpg", upload_to="logos")

    def __str__(self):
        return self.name

class Sport_League(models.Model):
    name = models.CharField(max_length=100,null=True)
    hostels = models.ManyToManyField("Hostel")
    format = models.ForeignKey("Format",  on_delete=models.CASCADE,null= True)
    final_points = models.JSONField(default=dict,null=True,blank=True)
    # logo = models.ImageField(default="default.jpg", upload_to="logos")

    def __str__(self):
        return self.name

class Status(models.Model):
    status = models.BooleanField(help_text="Enter 0 for upcoming and 1 for completed")

    def __str__(self):
        return self.status

class Stage(models.Model):
    stage = models.CharField(max_length=100)

    def __str__(self):
        return self.stage

class Match(models.Model):
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE,null= True)
    date_time = models.DateTimeField();
    team1 = models.ForeignKey("Hostel", related_name="team1", on_delete=models.CASCADE,null= True)
    team2 = models.ForeignKey("Hostel", related_name="team2", on_delete=models.CASCADE,null= True)
    stage = models.ForeignKey("Stage",  on_delete=models.CASCADE,null= True)
    score1 = models.IntegerField(null=True,blank=True)
    score2 = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.team1.name+" vs "+self.team2.name

class Match_all(models.Model):
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.ForeignKey("Status",  on_delete=models.CASCADE,null= True)
    date_time = models.DateTimeField()
    round = models.ForeignKey("Stage",  on_delete=models.CASCADE,null= True)

    def __str__(self):
        return self.team1.name+" vs "+self.team2.name

class Point(models.Model):
    hostels = models.ForeignKey("Hostel",  on_delete=models.CASCADE,null= True)
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    points = models.IntegerField()

    def __str__(self):
        return self.hostels.name

class Score(models.Model):
    hostels = models.ForeignKey("Hostel",  on_delete=models.CASCADE,null= True)
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    match = models.ForeignKey("Match_all",  on_delete=models.CASCADE,null= True)
    score = models.IntegerField()

    def __str__(self):
        return self.hostels.name