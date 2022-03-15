from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hostel,Point,Match
from .serializers import HostelSerializer,StandingSerializer,MatchSerializer

# Create your views here.

class OverallStandingsAPIView(ListCreateAPIView):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all().order_by('-overall_points')


class StandingsAPIView(ListCreateAPIView):
    serializer_class = StandingSerializer
    queryset = Point.objects.all()
    filterset_fields = ['sport']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['points']
    ordering = ['-points']
    search_fields = ['hostel__name','sport__name']

class MatchAPIView(ListCreateAPIView):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    filterset_fields = ['team1','team2','sport','date_time','status']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['date_time']
    ordering = ['-date_time']
    search_fields = ['team1__name','team2__name','status','sport__name']
