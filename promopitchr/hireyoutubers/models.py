from django.db import models
from datetime import datetime
# Create your models here.

class Hireyoutuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    youtuber_id = models.IntegerField(blank=True)
    youtuber_name = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True)
    city = models.CharField(max_length=255)
    phone = models.IntegerField()
    state = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    email = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email