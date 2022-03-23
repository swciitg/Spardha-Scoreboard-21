from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status,filters,response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from django.db.models import Q

# Create your views here.
class HostelAPIView(ListAPIView):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all().order_by('name')

class SportAPIView(ListAPIView):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()
    filterset_fields = ['name']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['name']
    ordering = ['name']
    search_fields = ['name','hostels__name']


class OverallStandingsAPIView(ListAPIView):
    # serializer_class = HostelSerializer
    # queryset = Hostel.objects.all().order_by('-overall_points')

    def get(self, request, *args, **kwargs):
        try:
            girls_hostels = Hostel.objects.all().filter(type=2).order_by('-overall_points')
            boys_hostels = Hostel.objects.all().filter(type=1).order_by('-overall_points')
            data = {}
            data["boys"] = []
            data["girls"] = []
            for hostel in boys_hostels:
                hostel_data = HostelSerializer(hostel).data
                data["boys"].append(hostel_data)
            
            for hostel in girls_hostels:
                hostel_data = HostelSerializer(hostel).data
                data["girls"].append(hostel_data)
            return response.Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StandingsAPIView(ListAPIView):
    serializer_class = StandingSerializer
    queryset = Point.objects.all()
    filterset_fields = ['sport']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['points']
    ordering = ['-points']
    search_fields = ['hostel__name','sport__name']

class MatchList(ListAPIView):

    def get(self, request, *args, **kwargs):
        hostelId = self.request.query_params.get('hostel')
        sportId = self.request.query_params.get('sport')
        def sorthelper(e):
            return e["date"]+"Z"+e["time"]
        # try:
        matchA = []
        matchB = []
        matchC = []
        matchD = []
        match_list = []
        if hostelId is None and sportId is None:
            matchA = MatchA.objects.all()
            matchB = MatchB.objects.all()
            matchC = MatchC.objects.all()
            matchD = MatchD.objects.all()
        elif sportId is None:
            hostel = Hostel.objects.get(id=hostelId)
            matchA = MatchA.objects.all().filter(Q(team1=hostel) | Q(team2=hostel))
            matchB = MatchB.objects.all().filter(Q(team1=hostel) | Q(team2=hostel))
            matchC = MatchC.objects.all().filter(Q(team1=hostel) | Q(team2=hostel))
            matchD = [match for match in MatchD.objects.all() if hostel in match.hostels.all()]
        elif hostelId is None:
            sport = Sport.objects.get(id=sportId)
            matchA = MatchA.objects.all().filter(sport=sport)
            matchB = MatchB.objects.all().filter(sport=sport)
            matchC = MatchC.objects.all().filter(sport=sport)
            matchD = MatchD.objects.all().filter(sport=sport)
        else:
            matchA = MatchA.objects.all().filter(sport=sport).filter(Q(team1=hostel) | Q(team2=hostel))
            matchB = MatchB.objects.all().filter(sport=sport).filter(Q(team1=hostel) | Q(team2=hostel))
            matchC = MatchC.objects.all().filter(sport=sport).filter(Q(team1=hostel) | Q(team2=hostel))
            matchD = [match for match in MatchD.objects.all().filter(sport=sport) if hostel in match.hostels.all()]

        for match in matchA:
            match_data = MatchASerializer(match).data
            match_data["type"] = "A"
            match_list.append(match_data)

        for match in matchB:
            match_data = MatchBSerializer(match).data
            match_data["type"] = "B"
            match_list.append(match_data)

        for match in matchC:
            match_data = MatchCSerializer(match).data
            match_data["type"] = "C"
            sets = Set.objects.all().filter(match = match)
            match_data["sets"] = []
            for set in sets:
                match_data["sets"].append(SetSerializer(set).data)
            match_list.append(match_data)

        for match in matchD:
            match_data = MatchDSerializer(match).data
            match_data["type"] = "D"
            match_list.append(match_data)

        match_list.sort(key=sorthelper,reverse=True)

        return response.Response({"data":match_list},status=status.HTTP_200_OK)
        
        # except Exception as e:
        #     print(e)
        #     return response.Response({"error":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class MatchAPIView(ListCreateAPIView):
#     serializer_class = MatchASerializer
#     queryset = MatchA.objects.all()
#     filterset_fields = ['id','status','team1','team2','sport','date']
#     filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
#     ordering_fields = ['date']
#     ordering = ['-date']
#     search_fields = ['team1__name','team2__name','sport__name']


# class MatchAllAPIView(ListAPIView):
#     serializer_class = MatchDSerializer
#     queryset = MatchD.objects.all()
#     filterset_fields = ['id','status','hostels','sport','date']
#     filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
#     ordering_fields = ['date']
#     ordering = ['-date']
#     search_fields = ['team1__name','team2__name','sport__name']

