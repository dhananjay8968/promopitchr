from django.shortcuts import render
from .models import Slider,Team,ProjectConfiguration
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    youtubers = Youtuber.objects.order_by('-created_date')
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'sliders' : sliders,
        'teams' : teams,
        'youtubers' : youtubers,
        'featured_youtubers' : featured_youtubers
    }
    return render(request,'webpages/home.html',data)

def about(request):
    project_configuration = ProjectConfiguration.objects.all().first()
    print(project_configuration)
    teams = Team.objects.all()
    data = {
        'teams': teams,
        'project_configuration': project_configuration
    }
    return render(request,'webpages/about.html',data)


def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    return render(request,'webpages/contact.html')
