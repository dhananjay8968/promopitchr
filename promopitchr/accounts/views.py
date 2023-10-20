from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from hireyoutubers.models import Hireyoutuber
from youtubers.models import Youtuber
# Create your views here.

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request,user)
            messages.warning(request,'You are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user_name = request.POST['user_name']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.warning(request,'username already exists in database')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=user_name,password=password)
                    user.save()
                    messages.success(request,'Account created successfully')
                    return redirect('login')
        else:
            messages.warning(request,'Passwords do not match')
            return redirect('register')
        

    return render(request,'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    youtubers_contacted_ids = list(Hireyoutuber.objects.filter(user_id=request.user.id).values_list('youtuber_id',flat=True).distinct())
    youtubers_contacted = Youtuber.objects.filter(pk__in=youtubers_contacted_ids)
    data = {
        'youtubers_contacted': youtubers_contacted
    }
    return render(request,'accounts/dashboard.html',data)
