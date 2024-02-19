from django.db import models
from rest_framework import serializers
from .models import TitleCard, PersonCard, AboutUs, MissionVision, BoardOfOrganization, UsefulLink, Gallery, GalleryImage, YouTubeLink, Downloads, Management, Tender, TenderFile


class TitleCardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = TitleCard
        fields = ['id', 'title', 'description']

    def get_id(self, obj):
        # Return the count of the current object
        return TitleCard.objects.filter(id__lte=obj.id).count()


class PersonCardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = PersonCard
        fields = ['id', 'name', 'designation', 'image', 'description']

    def get_id(self, obj):
        # Return the count of the current object
        return PersonCard.objects.filter(id__lte=obj.id).count()


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['description', 'image', 'subtitle', 'subcontent']


class MissionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVision
        fields = ['mission', 'vision']


class BoardOfOrganizationSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = BoardOfOrganization
        fields = '__all__'

    def get_id(self, obj):
        # Return the count of the current object
        return BoardOfOrganization.objects.filter(id__lte=obj.id).count()


class UsefulLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLink
        fields = ['name']


class YouTubeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeLink
        fields = ['name']


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['image']


class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'description', 'category', 'images']

    def get_id(self, obj):
        # Return the count of the current object
        return Gallery.objects.filter(id__lte=obj.id).count()


class DownloadsSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Downloads
        fields = ['id', 'title', 'file']

    def get_id(self, obj):
        # Return the count of the current object
        return Downloads.objects.filter(id__lte=obj.id).count()


class ManagementSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Management
        fields = '__all__'

    def get_id(self, obj):
        # Return the count of the current object
        return Management.objects.filter(id__lte=obj.id).count()


class TenderFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderFile
        fields = ['file']


class TenderSerializer(serializers.ModelSerializer):
    files = TenderFileSerializer(many=True, read_only=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Tender
        fields = '__all__'

    def get_id(self, obj):
        # Return the count of the current object
        return Tender.objects.filter(id__lte=obj.id).count()
