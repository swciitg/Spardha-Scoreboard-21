from django.urls import path,include
from .views import OverallStandingsAPIView,StandingsAPIView

urlpatterns = [
    path('standingsOverall/', OverallStandingsAPIView.as_view()),
    path('standings/', StandingsAPIView.as_view()),
]
