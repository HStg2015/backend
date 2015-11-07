import datetime

from rest_framework import filters
from rest_framework import viewsets

from api.models import RefugeeCamp, SimpleOffer, ObjectCategory, HelpTimeSearch
from api.serializers import RefugeeCampSerializer, SimpleOfferSerializer, ObjectCategorySerializer, HelpTimeSearchSerializer

class RefugeeCampViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RefugeeCamp.objects.all()
    serializer_class = RefugeeCampSerializer

class ObjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = ObjectCategory.objects.all()
    serializer_class = ObjectCategorySerializer

class SimpleOfferViewSet(viewsets.ModelViewSet):
    queryset = SimpleOffer.objects.all()
    serializer_class = SimpleOfferSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category',)

class HelpTimeRangeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        start_time = request.query_params.get('start_time', None)
        end_time = request.query_params.get('end_time', None)

        if not start_time or not end_time:
            return queryset

        return queryset.filter(date_time_field__range=(
            datetime.datetime.combine(start_time, datetime.time.min),
            datetime.datetime.combine(end_time, datetime.time.max))
        )

class HelpTimeSearchViewSet(viewsets.ModelViewSet):
    queryset = HelpTimeSearch.objects.all()
    serializer_class = HelpTimeSearchSerializer

    filter_backends = (HelpTimeRangeFilter,)
