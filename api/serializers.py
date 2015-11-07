from rest_framework import serializers

class RefugeeCampSerializer(serializers.Serializer):
    city = serializers.CharField()
    postcode = serializers.CharField()
    street = serializers.CharField()
    streetnumber = serializers.CharField()

class SimpleOfferSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

    city = serializers.CharField()
    telephone = serializers.CharField()
    email = serializers.EmailField()
