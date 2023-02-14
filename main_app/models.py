from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    members = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} artist by {self.user}"
    
    def get_absolute_url(self):
        return reverse('artist_details', kwargs={'pk': self.id})
    

class Experience(models.Model):
    MUSIC = 'MU'
    VIDEO = 'VI'
    SHOW = 'SH'
    MERCHANDISE = 'ME'
    SOCIAL_MEDIA = 'SO'
    NEWS = 'NE'
    EXPERIENCE_TYPE = [
        (MUSIC, 'Music'),
        (VIDEO, 'Video'),
        (SHOW, 'Show'),
        (MERCHANDISE, 'Merchandise'),
        (SOCIAL_MEDIA, 'Social Media'),
        (NEWS, 'News'),
    ]
    experience_type = models.CharField(
        max_length=2,
        choices=EXPERIENCE_TYPE
    )

    user_review = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    date_time = models.DateTimeField(
        blank=True,
        null=True
    )

    link = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    ALBUM = 'AL'
    SINGLE = 'SI'
    MIXTAPE = 'MI'
    EP = 'EP'
    FEATURE = 'FE'
    MUSIC_TYPE = [
        (ALBUM, 'Album'),
        (SINGLE, 'Single'),
        (MIXTAPE, 'Mixtape'),
        (EP, 'EP'),
        (FEATURE, 'Features On'),
    ]
    music_type = models.CharField(
        max_length=2,
        choices=MUSIC_TYPE,
        blank=True,
        null=True
    )

    show_venue_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.experience_type} experience on {self.artist}"
    
    def get_absolute_url(self):
        return reverse('artist_details', kwargs={'pk': self.id})


class Comment(models.Model):
    comment = models.TextField(max_length=250)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s comment on {self.experience}"
    
    # def get_absolute_url(self):
        # return reverse('comment_detail', kwargs={'comment_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Photo" 
        # Needs some improvement - passing into two different models.