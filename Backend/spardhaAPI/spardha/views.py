from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .models import Sport
from .serializers import SportSerializer
# Create your views here.
class StandingsAPIView(ListCreateAPIView):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()

    def get(self, request):
       data = {"kameng":20}
       return Response(data,status=HTTP_200_OK, content_type = 'application/json' )