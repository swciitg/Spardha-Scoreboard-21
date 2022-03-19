from django.urls import path
from .views import *
from .views import *

urlpatterns = [
    path('standingsOverall/', OverallStandingsAPIView.as_view()),
    path('standings/', StandingsAPIView.as_view()),
    path('matches/', MatchAPIView.as_view()),
    path('matchesAll/', MatchAllAPIView.as_view()),
    path('hostels/', HostelAPIView.as_view()),
    path('sports/', SportAPIView.as_view()),
]
