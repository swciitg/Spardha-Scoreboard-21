from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter,SearchFilter # Ordering filter is used to return results sorted to a specific field, searchfilter is used for searching
from .models import YourModel
from .serializers import YourModelSerializer
class SampleListAPIView(ListAPIView):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    filter_backends = (OrderingFilter, SearchFilter)  # adding this line will make drf magically include searching and sorting
    # in your api view (Check out the filtering options on the top of the page now appearing)
    ordering_fields = ('your_model_name_field','datetime','etc',) # Just add the fields with which you might wanna sort
    ordering = ('-datetime',) # this was used to specify default ordering as far as i remember, but i am not sure
    search_fields = ('your_model_name_field','your_model_field_2',)