from django.shortcuts import render,redirect
from .models import Hireyoutuber
from django.contrib import messages
# Create your views here.


def hireyoutuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        youtuber_id = request.POST['youtuber_id']
        youtuber_name = request.POST['youtuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']
        email = request.POST['email']
        user_id = request.POST['user_id']

        hireyoutuber_obj = Hireyoutuber(first_name=first_name,
                                        last_name=last_name,
                                        youtuber_id=youtuber_id,
                                        youtuber_name=youtuber_name,
                                        city=city,
                                        phone=phone,
                                        state=state,
                                        message=message,
                                        email=email,
                                        user_id=user_id
                                        )
        hireyoutuber_obj.save()
        messages.success(request,"Thank for reaching out")
        return redirect('youtubers')
        
