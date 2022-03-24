from django.urls import path
from .views import *
from .views import *

urlpatterns = [
    path('hostels/', HostelAPIView.as_view()),
    path('sports/', SportAPIView.as_view()),
    path('standingsOverall/', OverallStandingsAPIView.as_view()),
    path('standings/', StandingsAPIView.as_view()),
    path('matches/',MatchList.as_view())
]
