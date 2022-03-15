from django.urls import path,include
from .views import OverallStandingsAPIView,StandingsAPIView,MatchAPIView

urlpatterns = [
    path('standingsOverall/', OverallStandingsAPIView.as_view()),
    path('standings/', StandingsAPIView.as_view()),
    path('matches/', MatchAPIView.as_view()),
]
