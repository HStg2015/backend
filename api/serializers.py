from rest_framework import serializers

class RefugeeCampSerializer(serializers.Serializer):
    email = serializers.EmailField()
    city = serializers.CharField()
    postcode = serializers.CharField()
    street = serializers.CharField()
    streetnumber = serializers.CharField()

class SimpleOfferSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

    city = serializers.CharField()
    telnr = serializers.CharField()
    email = serializers.EmailField()
