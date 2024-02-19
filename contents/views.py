from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TitleCard, PersonCard, AboutUs, MissionVision, BoardOfOrganization, UsefulLink, Gallery, YouTubeLink, Downloads, Management, Tender
from .serializers import TitleCardSerializer, PersonCardSerializer, AboutUsSerializer, MissionVisionSerializer, BoardOfOrganizationSerializer, UsefulLinkSerializer, GallerySerializer, YouTubeLinkSerializer, DownloadsSerializer, ManagementSerializer, TenderSerializer


class TitleCardListAPIView(generics.ListAPIView):
    queryset = TitleCard.objects.all()
    serializer_class = TitleCardSerializer


class PersonCardListAPIView(generics.ListAPIView):
    queryset = PersonCard.objects.all()
    serializer_class = PersonCardSerializer


class ManagementListAPIView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class AboutUsAPIView(generics.RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get_object(self):
        # Retrieve the single AboutUs object
        return AboutUs.objects.first()


class MissionVisionAPIView(generics.RetrieveAPIView):
    queryset = MissionVision.objects.all()
    serializer_class = MissionVisionSerializer

    def get_object(self):
        # Retrieve the single AboutUs object
        return MissionVision.objects.first()


class BoardOfOrganizationListAPIView(generics.ListAPIView):
    queryset = BoardOfOrganization.objects.all()
    serializer_class = BoardOfOrganizationSerializer


class UsefulLinkListAPIView(generics.ListAPIView):
    queryset = UsefulLink.objects.all()
    serializer_class = UsefulLinkSerializer


class YouTubeLinkListAPIView(generics.ListAPIView):
    queryset = YouTubeLink.objects.all()
    serializer_class = YouTubeLinkSerializer


class GalleryListAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class DownloadsListAPIView(generics.ListAPIView):
    queryset = Downloads.objects.all()
    serializer_class = DownloadsSerializer


class TenderListAPIView(generics.ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer


class HomeAPIView(APIView):
    def get(self, request, format=None):
        # Get all TitleCard and PersonCard objects
        title_cards = TitleCard.objects.all()
        person_cards = PersonCard.objects.all()
        about_us = AboutUs.objects.all()
        mission_vision = MissionVision.objects.all()
        board_of_org = BoardOfOrganization.objects.all()
        useful_links = UsefulLink.objects.all()
        yt_links = YouTubeLink.objects.all()
        gallery_images = Gallery.objects.all()

        # Serialize the data
        title_card_serializer = TitleCardSerializer(title_cards, many=True)
        person_card_serializer = PersonCardSerializer(person_cards, many=True)
        about_us_serializer = AboutUsSerializer(about_us, many=True)
        mission_vision_serializer = MissionVisionSerializer(mission_vision, many=True)
        board_of_org_serializer = BoardOfOrganizationSerializer(board_of_org, many=True)
        useful_links_serializer = UsefulLinkSerializer(useful_links, many=True)
        gallery_images_serializer = GallerySerializer(gallery_images, many=True)
        yt_links_serializer = YouTubeLinkSerializer(yt_links, many=True)

        default_mission = "Default mission text goes here"
        default_vision = "Default mission text goes here"

        mission_vision_data = mission_vision_serializer.data

        if mission_vision_data and mission_vision_data[0].get('mission') and mission_vision_data[0].get('vision'):
            mission_text = mission_vision_data[0].get('mission')
            vision_text = mission_vision_data[0].get('vision')
        else:
            mission_text = default_mission
            vision_text = default_vision

        # Combine the serialized data
        data = {
            'title_cards': title_card_serializer.data,
            'person_cards': person_card_serializer.data,
            'about_us': about_us_serializer.data,
            'mission': mission_text,
            'vision': vision_text,
            'board_of_organisation': board_of_org_serializer.data,
            'useful_links': useful_links_serializer.data,
            'yt_links': yt_links_serializer.data,
            'gallery_images': gallery_images_serializer.data,
        }

        return Response(data)
