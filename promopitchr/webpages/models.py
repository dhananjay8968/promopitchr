from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=255)
    def __str__(self):
        return self.first_name
    
class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y')
    created_at = models.DateTimeField(auto_now_add=True)
    button_redirect_url = models.TextField(default="https://www.google.com")

    def __str__(self):
        return self.headline
    
class ProjectConfiguration(models.Model):
    about_us_description = RichTextField()
    about_us_image = models.ImageField(upload_to="media/promopitchr/%Y/%m/")
    contact_email = models.CharField(max_length=255)
    contact_phone = models.IntegerField()
    facebook_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.contact_email