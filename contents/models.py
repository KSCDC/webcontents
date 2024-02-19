from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone


class TitleCard(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Check if there are already three TitleCard instances
        if TitleCard.objects.count() >= 3:
            # If so, prevent saving new instances
            if self.pk is None:
                raise Exception("Cannot create more than 3 TitleCards")

        super().save(*args, **kwargs)


class PersonCard(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    designation = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(
        upload_to='person_cards/', blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if there are already four Person instances
        if PersonCard.objects.count() >= 4:
            # If so, prevent saving new instances
            if self.pk is None:
                raise Exception("Cannot create more than 4 PersonCards")

        super().save(*args, **kwargs)


class AboutUs(models.Model):
    description = models.TextField(max_length=3000, blank=False, null=False)
    image = models.ImageField(upload_to='about_us/', blank=False, null=False)
    subtitle = models.CharField(max_length=100)
    subcontent = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return "About Us"

    def save(self, *args, **kwargs):
        # Check if an AboutUs object already exists
        if AboutUs.objects.exists():
            # If so, prevent creating new instances
            if self.pk is None:
                raise Exception("Only one AboutUs object is allowed")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class MissionVision(models.Model):
    mission = models.TextField(
        max_length=3000, blank=False, null=False, default="mission")
    vision = models.TextField(
        max_length=3000, blank=False, null=False,  default="vision")

    def __str__(self):
        return "Mission and Vision"

    def save(self, *args, **kwargs):
        # Check if an AboutUs object already exists
        if MissionVision.objects.exists():
            # If so, prevent creating new instances
            if self.pk is None:
                raise Exception("Only one MissionVision object is allowed")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Mission & Vision"
        verbose_name_plural = "Mission & Vision"


class BoardOfOrganization(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    designation = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(
        upload_to='board_of_organization/', blank=False, null=False)
    email = models.EmailField(validators=[EmailValidator()])
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if there are already four Person instances
        if BoardOfOrganization.objects.count() >= 9:
            # If so, prevent saving new instances
            if self.pk is None:
                raise Exception(
                    "Cannot create more than 9 BoardOfOrganization members")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Board Of Organization"


class UsefulLink(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class YouTubeLink(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    CATEGORY_CHOICES = (
        ('functions', 'Functions'),
        ('achievements', 'Achievements'),
        ('awards', 'Awards'),
    )

    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Gallery"


class GalleryImage(models.Model):
    gallery = models.ForeignKey(
        Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return f"Image for {self.gallery.title}"


class Downloads(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='downloads/')

    def __str__(self):
        return self.title

    def upload_to(instance, filename):
        return 'downloads/{filename}'.format(filename=filename)

    class Meta:
        verbose_name_plural = "Downloads"


class Management(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(
        upload_to='management/', blank=False, null=False)
    email = models.EmailField(validators=[EmailValidator()])
    phone_number_one = models.CharField(max_length=20)
    phone_number_two = models.CharField(max_length=20, blank=True)
    phone_number_three = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if there are already four Person instances
        if Management.objects.count() >= 6:
            # If so, prevent saving new instances
            if self.pk is None:
                raise Exception("Cannot create more than 6 management")

        super().save(*args, **kwargs)


class Tender(models.Model):
    LIVE_TENDER = 'live'
    PREVIOUS_TENDER = 'previous'
    TENDER_CATEGORIES = [
        (LIVE_TENDER, 'Live Tender'),
        (PREVIOUS_TENDER, 'Previous Tender'),
    ]

    title = models.CharField(max_length=100)
    published_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField()
    is_e_tender = models.BooleanField(default=False)
    category = models.CharField(
        max_length=20, choices=TENDER_CATEGORIES, default=LIVE_TENDER)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.expiry_date < timezone.now().date():
            self.category = self.PREVIOUS_TENDER
        super().save(*args, **kwargs)


class TenderFile(models.Model):

    def upload_to(instance, filename):
        return f'tender_files/{instance.tender}/{filename}'

    tender = models.ForeignKey(
        Tender, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.file.name
