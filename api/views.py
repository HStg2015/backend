from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.models import RefugeeCamp, SimpleOffer
from api.serializers import RefugeeCampSerializer, SimpleOfferSerializer

class RefugeeCampViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RefugeeCamp.objects.all()
    serializer_class = RefugeeCampSerializer

class SimpleOfferViewSet(viewsets.ModelViewSet):
    queryset = SimpleOffer.objects.all()
    serializer_class = SimpleOfferSerializer
