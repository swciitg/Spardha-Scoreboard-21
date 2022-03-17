from django.contrib import admin
from .models import *

# Register your models here.

class HostelAdmin(admin.ModelAdmin):
    list_display = ['name','overall_points']
    ordering = ['overall_points']

class SportAdmin(admin.ModelAdmin):
    list_display = ['name','format']
    ordering = ['name']

class FormatAdmin(admin.ModelAdmin):
    list_display = ['format']
    ordering = ['format']

class StageAdmin(admin.ModelAdmin):
    list_display = ['stage']
    ordering = ['stage']

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['sport','hostel']
    ordering = ['sport']

class PointAdmin(admin.ModelAdmin):
    list_display = ['sport','hostel','points']
    list_filter = ['sport','hostel']
    ordering = ['sport','-points']

class MatchAdmin(admin.ModelAdmin):
    list_display = ['name','sport','stage','date_time','status']
    list_filter = ['status','sport','stage','team1','team2',]
    ordering = ['date_time']

class MatchAllAdmin(admin.ModelAdmin):
    list_display = ['sport','date_time','status']
    list_filter = ['status','sport','round']
    ordering = ['date_time']

admin.site.register(Hostel,HostelAdmin)
admin.site.register(Format,FormatAdmin)
admin.site.register(Sport,SportAdmin)
admin.site.register(Match,MatchAdmin)
admin.site.register(Match_all,MatchAllAdmin)
admin.site.register(Stage,StageAdmin)
admin.site.register(Point,PointAdmin)
admin.site.register(Score,ScoreAdmin)