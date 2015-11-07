import datetime

from rest_framework import filters
from rest_framework import viewsets

from api import models, serializers

class RefugeeCampViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RefugeeCamp.objects.all()
    serializer_class = serializers.RefugeeCampSerializer

class ObjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ObjectCategory.objects.all()
    serializer_class = serializers.ObjectCategorySerializer

class ObjectSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ObjectSubCategory.objects.all()
    serializer_class = serializers.ObjectSubCategorySerializer

class SimpleOfferViewSet(viewsets.ModelViewSet):
    queryset = models.SimpleOffer.objects.all()
    serializer_class = serializers.SimpleOfferSerializer

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
    queryset = models.HelpTimeSearch.objects.all()
    serializer_class = serializers.HelpTimeSearchSerializer

    filter_backends = (HelpTimeRangeFilter,)
