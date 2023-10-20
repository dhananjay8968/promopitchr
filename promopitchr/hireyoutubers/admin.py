from django.contrib import admin
from .models import Hireyoutuber
# Register your models here.


class HireyoutuberAdmin(admin.ModelAdmin):
    list_display = ['youtuber_name','first_name','email']
    list_display_links = ['youtuber_name']
    list_filter = ['youtuber_name']
admin.site.register(Hireyoutuber,HireyoutuberAdmin)