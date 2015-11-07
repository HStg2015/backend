from rest_framework import serializers
from rest_framework import relations
from api.models import SimpleOffer, ObjectCategory, HelpTimeOffer

class RefugeeCampSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    city = serializers.CharField()
    postcode = serializers.CharField()
    street = serializers.CharField()
    streetnumber = serializers.CharField()

class ObjectCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField()

    def create(self, validated_data):
        return ObjectCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

class SimpleOfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    category = relations.PrimaryKeyRelatedField(queryset=ObjectCategory.objects.all())
    title = serializers.CharField()
    description = serializers.CharField()
    create_time = serializers.DateTimeField()
    image = serializers.ImageField(allow_null=True)

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
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.city = validated_data.get('city', instance.city)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class HelpTimeOfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    email = serializers.EmailField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return HelpTimeOffer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
