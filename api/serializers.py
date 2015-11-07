from rest_framework import serializers
from rest_framework import relations
from api.models import RefugeeCamp, SimpleOffer, ObjectCategory, ObjectSubCategory, HelpTimeSearch

class RefugeeCampSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    city = serializers.CharField(max_length=64)
    postcode = serializers.CharField(max_length=16)
    street = serializers.CharField(max_length=128)
    streetnumber = serializers.CharField(max_length=32)

class ObjectCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=64)

    def create(self, validated_data):
        return ObjectCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

class SimpleOfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    category = relations.PrimaryKeyRelatedField(queryset=ObjectCategory.objects.all())
    title = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=4096)
    create_time = serializers.DateTimeField()
    image = serializers.ImageField(allow_null=True)

    city = serializers.CharField(max_length=64)
    telephone = serializers.CharField(max_length=64)
    email = serializers.EmailField(max_length=128)

    def create(self, validated_data):
        return SimpleOffer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.city = validated_data.get('city', instance.city)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class HelpTimeSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    camp = relations.PrimaryKeyRelatedField(queryset=RefugeeCamp.objects.all())

    def create(self, validated_data):
        return HelpTimeSearch.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.camp = validated_data.get('camp', instance.camp)
        instance.save()
        return instance
