from rest_framework import serializers
from api.models import SimpleOffer

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

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return SimpleOffer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    