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
    list_display = ['name','type','overall_points']
    ordering = ['-overall_points']

# class FormatAdmin(admin.ModelAdmin):
#     list_display = ['format']
#     ordering = ['format']

class PointInline(admin.StackedInline):
    model = Point
    fieldsets = (
        (None, {
            'fields': ('sport',('hostel','points'),)
        }),
    )
class SportAdmin(admin.ModelAdmin):
    list_display = ['name','format']
    list_filter = ['format']
    ordering = ['name']
    inlines = (PointInline, )

class StageAdmin(admin.ModelAdmin):
    list_display = ['stage']
    ordering = ['stage']

class PointAdmin(admin.ModelAdmin):
    list_display = ['sport','hostel','points']
    list_filter = ['sport','hostel']
    ordering = ['sport','-points']

    
class MatchAAdmin(admin.ModelAdmin):
    list_display = ['name','sport','stage','date','time','status',]
    list_filter = ['status','sport','stage','team1','team2',]
    ordering = ['-date']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sport":
            kwargs["queryset"] = Sport.objects.filter(format=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class GameInline(admin.StackedInline):
    model = Game
class MatchBAdmin(admin.ModelAdmin):
    inlines = (GameInline, )
    list_display = ['name','sport','stage','date','time','status',]
    list_filter = ['status','sport','stage','team1','team2',]
    ordering = ['-date']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sport":
            kwargs["queryset"] = Sport.objects.filter(format=2)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SetInline(admin.StackedInline):
    model = Set
    fieldsets = (
        (None, {
            'fields': ('name',('team1_game1','team1_game2','team1_game3','team1_game4','team1_game5',),('team2_game1','team2_game2','team2_game3','team2_game4','team2_game5',))
        }),
    )
class MatchCAdmin(admin.ModelAdmin):
    inlines = (SetInline, )
    list_display = ['name','sport','stage','date','time','status',]
    list_filter = ['status','sport','stage','team1','team2',]
    ordering = ['-date']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sport":
            kwargs["queryset"] = Sport.objects.filter(format=3)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ScoreInline(admin.StackedInline):
    model = Score
    fieldsets = (
        (None, {
            'fields': ('match',('hostel','score'),)
        }),
    )
class MatchDAdmin(admin.ModelAdmin):
    list_display = ['sport','round', 'date','time','status']
    list_filter = ['status','sport','round']
    ordering = ['date']
    inlines = (ScoreInline, )
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sport":
            kwargs["queryset"] = Sport.objects.filter(format=4)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['match','hostel','score']
    ordering = ['match']


class MatchSetAdmin(admin.ModelAdmin):
    list_display = ['name','sport','date','time','status']
    list_filter = ['status','sport','team1','team2',]
    ordering = ['date']



admin.site.register(Hostel,HostelAdmin)
admin.site.register(Sport,SportAdmin)
admin.site.register(Stage,StageAdmin)
admin.site.register(Point,PointAdmin)
admin.site.register(Score,ScoreAdmin)
admin.site.register(MatchA,MatchAAdmin)
admin.site.register(MatchD,MatchDAdmin)
admin.site.register(MatchB,MatchBAdmin)
admin.site.register(MatchC,MatchCAdmin)