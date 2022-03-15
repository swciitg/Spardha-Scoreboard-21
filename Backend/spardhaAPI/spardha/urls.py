from django.urls import path,include
from .views import OverallStandingsAPIView,StandingsAPIView,MatchAPIView
from .views import *

urlpatterns = [
    path('standingsOverall/', OverallStandingsAPIView.as_view()),
    path('standings/', StandingsAPIView.as_view()),
    path('matches/', MatchAPIView.as_view()),

    path('<int:pk>/updatePoints/', UpdatePoints.as_view(),name='points-update'),
]
