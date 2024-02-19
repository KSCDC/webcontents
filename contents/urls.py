from django.urls import path
from .views import TitleCardListAPIView, PersonCardListAPIView, HomeAPIView, AboutUsAPIView, MissionVisionAPIView, BoardOfOrganizationListAPIView, UsefulLinkListAPIView, GalleryListAPIView, YouTubeLinkListAPIView, DownloadsListAPIView, ManagementListAPIView, TenderListAPIView


urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('titlecard/', TitleCardListAPIView.as_view(), name='titlecard-list'),
    path('personcard/', PersonCardListAPIView.as_view(), name='personcard-list'),
    path('aboutus/', AboutUsAPIView.as_view(), name='aboutus'),
    path('missionvision/', MissionVisionAPIView.as_view(), name='missionvision'),
    path('boardoforg/', BoardOfOrganizationListAPIView.as_view(),
         name='board-of-organisation'),
    path('links/', UsefulLinkListAPIView.as_view(), name='links'),
    path('ytlinks/', YouTubeLinkListAPIView.as_view(), name='yt-links'),
    path('gallery/', GalleryListAPIView.as_view(), name='gallery-list'),
    path('downloads/', DownloadsListAPIView.as_view(), name='downloads'),
    path('management/', ManagementListAPIView.as_view(), name='management'),
    path('tenders/', TenderListAPIView.as_view(), name='tender')




]
