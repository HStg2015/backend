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

class HelpTimeSearchViewSet(viewsets.ModelViewSet):
    queryset = HelpTimeSearch.objects.all()
    serializer_class = HelpTimeSearchSerializer
