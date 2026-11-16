from django.shortcuts import render, redirect, get_object_or_404
from .models import profile, Ride
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required


# Home Page
def home(request):
    return render(request, 'home.html')


# User Registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        if role not in ['CUSTOMER', 'DRIVER']:
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        profile.objects.create(
            user=user,
            role=role
        )

        return redirect('login')

    return render(request, 'register.html')


# User Login
def loginuser(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


# User Logout
@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


# Book a Ride
@login_required
def bookride(request):

    if request.method == 'POST':
        Ride.objects.create(
            customer=request.user,
            pickup_location=request.POST['pickup_location'],
            drop_location=request.POST['drop_location'],
            fare=150
        )

        return redirect('my_rides')

    return render(request, 'bookride.html')


# Customer My Rides
@login_required
def myrides(request):

    rides = Ride.objects.filter(
        customer=request.user
    )

    return render(request, 'my_rides.html', {'rides': rides})


# Available Rides for Drivers
@login_required
def available_rides(request):

    user_profile = get_object_or_404(profile, user=request.user)

    if user_profile.role != 'DRIVER':
        return redirect('home')

    rides = Ride.objects.filter(
        status='REQUESTED',
        driver__isnull=True
    )

    return render(request, 'available_rides.html', {'rides': rides})


# Accept Ride
@login_required
def accept_ride(request, ride_id):

    user_profile = get_object_or_404(profile, user=request.user)

    if user_profile.role != 'DRIVER':
        return redirect('home')

    ride = get_object_or_404(
        Ride,
        id=ride_id,
        status='REQUESTED',
        driver__isnull=True
    )

    ride.driver = request.user
    ride.status = 'ACCEPTED'
    ride.save()

    return redirect('drive_rides')


# Driver Assigned Rides
@login_required
def drive_rides(request):

    user_profile = get_object_or_404(profile, user=request.user)

    if user_profile.role != 'DRIVER':
        return redirect('home')

    rides = Ride.objects.filter(
        driver=request.user
    )

    return render(request, 'driver_rides.html', {'rides': rides})


# Update Ride Status
@login_required
def update_status(request, ride_id, status):

    user_profile = get_object_or_404(profile, user=request.user)

    if user_profile.role != 'DRIVER':
        return redirect('home')

    ride = get_object_or_404(
        Ride,
        id=ride_id,
        driver=request.user
    )

    allowed_status = ['STARTED', 'COMPLETED']

    if status not in allowed_status:
        return redirect('drive_rides')

    if status == 'STARTED' and ride.status == 'ACCEPTED':
        ride.status = 'STARTED'

    elif status == 'COMPLETED' and ride.status == 'STARTED':
        ride.status = 'COMPLETED'

    ride.save()

    return redirect('drive_rides')