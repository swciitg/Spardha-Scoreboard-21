from email.policy import default
from django import forms
from django.contrib import admin
from .models import *
from django.contrib.admin.utils import flatten_fieldsets
# Register your models here.

import json

from django.db.models import JSONField 
from django.contrib import admin
from django.forms import widgets

class HostelAdmin(admin.ModelAdmin):
    list_display = ['name','overall_points']
    ordering = ['overall_points']

class SportAdmin(admin.ModelAdmin):
    list_display = ['name','format']
    list_filter = ['format']
    ordering = ['name']

class FormatAdmin(admin.ModelAdmin):
    list_display = ['format']
    ordering = ['format']

class StageAdmin(admin.ModelAdmin):
    list_display = ['stage']
    ordering = ['stage']

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['match','hostel','score']
    ordering = ['match']

class PointAdmin(admin.ModelAdmin):
    list_display = ['sport','hostel','points']
    list_filter = ['sport','hostel']
    ordering = ['sport','-points']

class MatchAdmin(admin.ModelAdmin):
    list_display = ['name','sport','stage','date','time','status']
    list_filter = ['status','sport','stage','team1','team2',]
    ordering = ['date']

class MatchSetAdmin(admin.ModelAdmin):
    list_display = ['name','sport','date','time','status']
    list_filter = ['status','sport','team1','team2',]
    ordering = ['date']

class MatchAllForm(forms.ModelForm):

    class Meta:
        model = MatchD
        exclude = []
    def __init__(self, *args, **kwargs):
        # print("Called")
        super().__init__(*args, **kwargs)
        for hostel in Hostel.objects.all():
            if hostel in self.instance.hostels.all():
                try:
                    score = Score.objects.get(hostel = hostel, match=self.instance).score
                except:
                    scoreObj = Score.objects.create(hostel = hostel, match = self.instance, score = 0)
                    scoreObj.save()
                    score = scoreObj.score
            else:
                score = "NIL"
            if score == "NIL":
                self.base_fields[hostel.name] = forms.CharField(initial=score,disabled=True)
                self.fields[hostel.name] = forms.CharField(initial=score,disabled=True)
            else:
                self.base_fields[hostel.name] = forms.CharField(initial=score)
                self.fields[hostel.name] = forms.CharField(initial=score)


    def save(self, *args, **kwargs):
        # print(self.cleaned_data)
        for hostel in self.instance.hostels.all():
            score = Score.objects.get(hostel=hostel,match=self.instance)
            score.score = self.cleaned_data[hostel.name]
            score.save()
        return super().save(*args, **kwargs)

class MatchAllAdmin(admin.ModelAdmin):
    list_display = ['sport','round', 'date','time','status']
    list_filter = ['status','sport','round']
    ordering = ['date']
    customChangeForm = MatchAllForm
    # formfield_overrides = {
    #     JSONField: {'widget': PrettyJSONWidget}
    # }
    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during foo creation
        """
        if obj is not None:
            return MatchAllForm
        return super().get_form(request, obj, **kwargs)

admin.site.register(Hostel,HostelAdmin)
admin.site.register(Format,FormatAdmin)
admin.site.register(Sport,SportAdmin)
admin.site.register(MatchA,MatchAdmin)
admin.site.register(MatchD,MatchAllAdmin)
admin.site.register(Stage,StageAdmin)
admin.site.register(Point,PointAdmin)
admin.site.register(Score,ScoreAdmin)
admin.site.register(Match_set,MatchSetAdmin)