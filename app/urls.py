
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logout, name='logout'),

    # Customer
    path('book/', views.bookride, name='book_ride'),
    path('my-rides/', views.myrides, name='my_rides'),

    # Driver
    path('available-rides/', views.available_rides, name='available_rides'),
    path('accept/<int:ride_id>/', views.accept_ride, name='accept_ride'),
    path('driver-rides/', views.drive_rides, name='drive_rides'),

    # Ride Status
    path('status/<int:ride_id>/<str:status>/',
         views.update_status, name='update_status'),
]




    