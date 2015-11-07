from rest_framework import serializers
from api.models import SimpleOffer

class RefugeeCampSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    city = serializers.CharField()
    postcode = serializers.CharField()
    street = serializers.CharField()
    streetnumber = serializers.CharField()

class SimpleOfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField()

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
        instance.image = validated_data.get('image', instance.image)
        instance.city = validated_data.get('city', instance.city)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
