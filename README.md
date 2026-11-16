# Cab Booking System

## About the Project

Cab Booking System is a web application developed using Python and Django.

This application allows customers to book cab rides and drivers to view and accept available ride requests.

The main purpose of this project is to manage cab bookings and understand Django web application development.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

## Features

### Customer
- User Registration
- User Login and Logout
- Book a Cab
- View My Rides
- Check Ride Status

### Driver
- Driver Login
- View Available Rides
- Accept Ride Requests
- View Assigned Rides
- Update Ride Status

## Project Structure

```text
cab_booking/
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── cab_booking/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd cab_booking
```

**3. Install Django**

```bash
pip install django
```

**4. Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Run the development server**

```bash
python manage.py runserver
```

**6. Open in browser**

```text
http://127.0.0.1:8000/
```

## Database

This project uses SQLite to store user profiles, ride details, customer information, driver information, and ride status.

## What I Learned

- Django Project and App Structure
- Django Models
- Database Relationships
- User Authentication
- URL Routing
- Django Views
- CRUD Operations
- HTML Templates

## Author

**Janish**