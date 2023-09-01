from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from .forms import *
from django.contrib import messages
# Create your views here.

def home(request):
    # You can fetch featured cars or any other data you want to display on the home page
    featured_cars = Car.objects.filter(car_status='active')[:5]
    context = {'featured_cars': featured_cars}
    return render(request, 'car/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if not User.objects.filter(username=email).exists():
                user = User.objects.create_user(username=email, email=email, password=password)
                auth_login(request, user)
                messages.success(request, 'You have successfully registered.')
                return redirect('login')
            else:
                messages.error(request, 'A user with this email already exists.')

    else:
        form = UserRegistrationForm()

    return render(request, 'car/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'car/login.html')

    return render(request, 'car/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, f'Successfully Logged out, {request.user.username}.')

    return redirect('user_logout')



def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added the car.')
            return redirect('home')
    else:
        form = CarForm()
    
    return render(request, 'create_car.html', {'form': form})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car/car_detail.html', {'car': car})


def update_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated your profile, {request.user.username}.')

            return redirect('home')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'car/update_profile.html', {'form': form})