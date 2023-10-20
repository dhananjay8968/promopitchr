from django.shortcuts import render
from .models import Youtuber
from django.shortcuts import get_object_or_404
# Create your views here.

def youtubers(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        youtubers = youtubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        youtubers = youtubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        youtubers = youtubers.filter(camera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        youtubers = youtubers.filter(category__iexact=category)


    data = {
        'youtubers' : youtubers,
        'city_search' : city_search,
        'camera_search' : camera_search,
        'category_search' : category_search
    }
    
    return render(request,'youtubers/youtubers.html',data)

def youtubers_detail(request,id):
    youtuber = get_object_or_404(Youtuber,id=id)
    data = {
        'youtuber' : youtuber
    }
    return render(request,'youtubers/youtubers_detail.html',data)

def search(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        youtubers = youtubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        youtubers = youtubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        youtubers = youtubers.filter(camera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        youtubers = youtubers.filter(category__iexact=category)


    data = {
        'youtubers' : youtubers,
        'city_search' : city_search,
        'camera_search' : camera_search,
        'category_search' : category_search
    }


    return render(request,'youtubers/search.html',data)
