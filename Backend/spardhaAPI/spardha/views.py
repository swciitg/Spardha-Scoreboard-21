from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
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
    filterset_fields = ['team1','team2','sport','date_time']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['date_time']
    ordering = ['-date_time']
    search_fields = ['team1__name','team2__name','sport__name']

class MatchAPIView(ListCreateAPIView):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    filterset_fields = ['id','status','team1','team2','sport','date_time']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['date_time']
    ordering = ['-date_time']
    search_fields = ['team1__name','team2__name','sport__name']


class MatchAllAPIView(ListCreateAPIView):
    serializer_class = MatchSerializer
    queryset = Match_all.objects.all()
    filterset_fields = ['id','status','hostels','sport','date_time']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['date_time']
    ordering = ['-date_time']
    search_fields = ['team1__name','team2__name','sport__name']


class HostelAPIView(ListCreateAPIView):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all().order_by('name')

class SportAPIView(ListCreateAPIView):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()
    filterset_fields = ['name']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['name']
    ordering = ['name']
    search_fields = ['name','hostels__name']