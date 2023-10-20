from django.urls import path
from . import views

urlpatterns = [
    path('hireyoutuber/',views.hireyoutuber,name='hireyoutuber'),
]