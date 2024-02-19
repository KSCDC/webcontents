from django.contrib import admin
from .models import TitleCard, PersonCard, AboutUs, MissionVision, BoardOfOrganization, UsefulLink, Gallery, GalleryImage, YouTubeLink, Downloads, Management, Tender, TenderFile
from django import forms


class TitleCardAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if TitleCard.objects.count() >= 3:
            return False
        else:
            return True


class PersonCardAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if PersonCard.objects.count() >= 4:
            return False
        else:
            return True


class ManagementAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Management.objects.count() >= 6:
            return False
        else:
            return True


class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AboutUs.objects.exists():
            return False
        else:
            return True


class MissionVisionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if MissionVision.objects.exists():
            return False
        else:
            return True


class BoardOfOrganizationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if BoardOfOrganization.objects.count() >= 9:
            return False
        else:
            return True


admin.site.register(TitleCard, TitleCardAdmin)
admin.site.register(PersonCard, PersonCardAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(MissionVision, MissionVisionAdmin)
admin.site.register(BoardOfOrganization, BoardOfOrganizationAdmin)
admin.site.register(UsefulLink)
admin.site.register(YouTubeLink)
admin.site.register(Management, ManagementAdmin)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]


admin.site.register(Downloads)


class TenderFileInline(admin.TabularInline):
    model = TenderFile


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [TenderFileInline]
