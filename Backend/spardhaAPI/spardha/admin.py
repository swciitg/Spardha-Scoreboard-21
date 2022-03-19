from django import forms
from django.contrib import admin
from .models import *

# Register your models here.

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
    list_filter = ['match','hostel']
    ordering = ['match']

class PointAdmin(admin.ModelAdmin):
    list_display = ['sport','hostel','points']
    list_filter = ['sport','hostel']
    ordering = ['sport','-points']

class MatchAdmin(admin.ModelAdmin):
    list_display = ['name','sport','stage','date','time','status']
    list_filter = ['status','sport','stage','team1','team2',]
    ordering = ['date']

# class MatchAllForm(forms.ModelForm):
#     first_name = forms.CharField()
#     sport = forms.ModelChoiceField(queryset=Sport.objects.filter(format=2))

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         try:
#             print(self.instance.hostels)
#             scores = Score.objects.filter(match=self.instance)
#             print(self.instance)
#             print("alpha test 1")
#             for i in range(len(scores) + 1):
#                 field_name = 'score_%s' % (i,)
#                 self.fields[field_name] = forms.IntegerField(required=False)
#                 try:
#                     self.initial[field_name] = scores[i].interest
#                 except IndexError:
#                     self.initial[field_name] = 0
#             # create an extra blank field
#             field_name = 'score_%s' % (i + 1,)
#             self.fields[field_name] = forms.IntegerField(required=False)
#         except:
#             pass


class MatchAllAdmin(admin.ModelAdmin):
    list_display = ['sport','round', 'date','time','status']
    list_filter = ['status','sport','round']
    ordering = ['date']
    # form = MatchAllForm

admin.site.register(Hostel,HostelAdmin)
admin.site.register(Format,FormatAdmin)
admin.site.register(Sport,SportAdmin)
admin.site.register(Match,MatchAdmin)
admin.site.register(Match_all,MatchAllAdmin)
admin.site.register(Stage,StageAdmin)
admin.site.register(Point,PointAdmin)
admin.site.register(Score,ScoreAdmin)
