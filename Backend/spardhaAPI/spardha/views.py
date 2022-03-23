from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status,filters,response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from django.db.models import Q

# Create your views here.

class OverallStandingsAPIView(ListAPIView):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all().order_by('-overall_points')

    def get(self, request, *args, **kwargs):
        try:
            girls_hostels = Hostel.objects.all().filter(type="Girls").order_by('-overall_points')
            boys_hostels = Hostel.objects.all().filter(type="Boys").order_by('-overall_points')
            data = {}
            data["boys"] = []
            data["girls"] = []
            for hostel in boys_hostels:
                hostel_data = HostelSerializer(hostel)
                data["boys"].append(hostel_data)
            
            for hostel in girls_hostels:
                hostel_data = HostelSerializer(hostel)
                data["girls"].append(hostel_data)
            return response.Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({"error":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MatchList(ListAPIView):

    def get(self, request, *args, **kwargs):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Match.objects.all()
        hostel = self.request.query_params.get('hostel')
        sport = self.request.query_params.get('sport')
        def sorthelper(e):
            return e["date"]+"Z"+e["time"]
        try:
            match1v1=[]
            matchall = []
            match_list = []
            if hostel is None and sport is None:
                match1v1 = Match.objects.all()
                matchall = Match_all.objects.all()
                # print(h in matchall[0].hostels.all())
            elif sport is None:
                h = Hostel.objects.get(id=hostel)
                match1v1 = Match.objects.all().filter(Q(team1=hostel) | Q(team2=hostel))
                matchall = [match for match in Match_all.objects.all() if h in match.hostels.all()]
            elif hostel is None:
                match1v1 = Match.objects.all().filter(sport=sport)
                matchall = Match_all.objects.all().filter(sport=sport)
            else:
                match1v1 = Match.objects.all().filter(sport=sport).filter(Q(team1=hostel) | Q(team2=hostel))
                matchall = [match for match in Match_all.objects.all().filter(sport=sport) if h in match.hostels.all()]
            
            for match in match1v1:
                match_data = MatchSerializer(match).data
                match_data["type"] = "1v1"
                match_list.append(match_data)
                
            for match in matchall:
                match_data = MatchAllSerializer(match).data
                match_data['type'] = "all"
                match_list.append(match_data)
            match_list.sort(key=sorthelper)
            return response.Response({"data":match_list},status=status.HTTP_200_OK)
            
        except:
            return response.Response({"error":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
    filterset_fields = ['id','status','team1','team2','sport','date']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['date']
    ordering = ['-date']
    search_fields = ['team1__name','team2__name','sport__name']


class MatchAllAPIView(ListCreateAPIView):
    serializer_class = MatchAllSerializer
    queryset = Match_all.objects.all()
    filterset_fields = ['id','status','hostels','sport','date']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['date']
    ordering = ['-date']
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

