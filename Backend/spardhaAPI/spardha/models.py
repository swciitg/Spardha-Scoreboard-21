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

    def __str__(self):
        return self.name

class Stage(models.Model):
    stage = models.CharField(max_length=100)

    def __str__(self):
        return self.stage

class Match(models.Model):
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    status = models.BooleanField(default= False,help_text="Enter 0 for upcoming and 1 for completed") 
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    team1 = models.ForeignKey("Hostel", related_name="team1", on_delete=models.CASCADE,null= True)
    team2 = models.ForeignKey("Hostel", related_name="team2", on_delete=models.CASCADE,null= True)
    stage = models.ForeignKey("Stage",  on_delete=models.CASCADE,null= True)
    score1 = models.IntegerField(null=True,blank=True)
    score2 = models.IntegerField(null=True,blank=True)

    @property
    def name(self):
        return self.team1.name+" vs "+self.team2.name

class Match_all(models.Model):
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

    # def save(self, *args, **kwargs):
    #     super(Match_all, self).save(*args, **kwargs)
    #     print(self.hostels.all())
    #     for hostel in self.hostels.all():
    #         score = Score.objects.create(hostel = hostel,match=self,score=0)
    #         print(score)
    #         score.save()

class Point(models.Model):
    hostel = models.ForeignKey("Hostel", related_name="hostels", on_delete=models.CASCADE,null= True)
    sport = models.ForeignKey("Sport",  on_delete=models.CASCADE,null= True)
    points = models.IntegerField()

    class Meta:
        unique_together = ('hostel', 'sport',)

    def __str__(self):
        return self.sport.name+" ( "+self.hostel.name+" ) "

class Score(models.Model):
    hostel = models.ForeignKey("Hostel", related_name="hostel", on_delete=models.CASCADE,null= True)
    match = models.ForeignKey("Match_all",  on_delete=models.CASCADE,null= True)
    score = models.IntegerField()

    class Meta:
        unique_together = ('hostel', 'match',)

    def __str__(self):
        return self.match.name+" ( "+self.hostel.name+" ) "
