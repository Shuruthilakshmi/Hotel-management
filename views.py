from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import  Room, Booking
from .forms import BookingForm, RoomForm
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate
from django.urls import reverse_lazy
from django.contrib.auth.models import User
   # View for listing available rooms
from .models import Booking
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'hotel/home.html')

def about(request):
    return render(request, 'hotel/about.html')

def infrastructure(request):
    return render(request, 'hotel/infrastructure.html')

def room_list(request):
    available_rooms = Room.objects.filter(is_available=True)
    return render(request, 'hotel/room_list.html', {'rooms': available_rooms})

   # View for creating a booking
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')
        else:
            return render(request, 'hotel/book_room.html', {'form': form})
    else:
        form = BookingForm()
    return render(request, 'hotel/book_room.html', {'form': form})


def booked_rooms(request):
    bookings = Booking.objects.all()  # Retrieve all bookings
    return render(request, 'hotel/booked_rooms.html', {'bookings': bookings})


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booked_rooms')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'hotel/edit_booking.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()  # Delete the booking
        return redirect('booked_rooms')
    return render(request, 'hotel/cancel_booking.html', {'booking': booking})


   # Booking confirmation view
def booking_confirmation(request):
    try:
        bookings = Booking.objects.all()
    except Booking.DoesNotExist:
        bookings = None
    return render(request, 'hotel/booking_confirmation.html',{'bookings': bookings})

from django.shortcuts import render, redirect
from django.conf import settings

# Define the correct password here or use environment variable
CORRECT_PASSWORD = 'nsvp@4'

def create_room(request):
    if request.method == 'POST':
        # Check if the password was submitted in the form
        if 'password' in request.POST:
            entered_password = request.POST.get('password')
            if entered_password == CORRECT_PASSWORD:
                # Password is correct, show the room creation form
                form = RoomForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    return redirect('view_rooms')
                return render(request, 'hotel/create_room.html', {'form': form, 'authenticated': True})
            else:
                # Password is incorrect, show an error message
                return render(request, 'hotel/create_room.html', {'error': 'Incorrect password', 'authenticated': False})
        else:
            # If the form is submitted without a password (e.g., directly trying to access room creation)
            form = RoomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view_rooms')
    else:
        # Initial form display with password prompt
        return render(request, 'hotel/create_room.html', {'authenticated': False})

# View Rooms
from django.shortcuts import render, redirect
from django.conf import settings

# Define the correct password here or use environment variable
CORRECT_PASSWORD = 'nsvp@4'

def view_rooms(request):
    if request.method == 'POST':
        # Check if the password was submitted
        if 'password' in request.POST:
            entered_password = request.POST.get('password')
            if entered_password == CORRECT_PASSWORD:
                # Password is correct, show the room list
                rooms = Room.objects.all()
                return render(request, 'hotel/view_rooms.html', {'rooms': rooms, 'authenticated': True})
            else:
                # Password is incorrect, show an error message
                return render(request, 'hotel/view_rooms.html', {'error': 'Incorrect password', 'authenticated': False})
    else:
        # Initial form display with password prompt
        return render(request, 'hotel/view_rooms.html', {'authenticated': False})


# Update Room
def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('view_rooms')
    else:
        form = RoomForm(instance=room)
    return render(request, 'hotel/update_room.html', {'form': form})

# Delete Room
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return redirect('view_rooms')

def view_booked_rooms(request):
    # Filter rooms where is_available is False (booked rooms)
    booked_rooms = Room.objects.filter(is_available=False)
    return render(request, 'hotel/view_booked_rooms.html', {'booked_rooms': booked_rooms})

#def update(room_id):
    #room = get_object_or_404(Room, id=room_id)
    #room.is_available =False



@login_required
def cancel_booking(request, room_id):
    booking = get_object_or_404(Booking, id=room_id, user=request.user)
    
    if request.method == 'POST':
        booking.status = 'canceled'
        booking.save()

        return redirect('booking_confirmation')  # Redirect to a confirmation page

    return render(request, 'hotel/cancel_booking.html', {'booking': booking})

@staff_member_required
def delete_booking(request, room_id):
    booking = get_object_or_404(Booking, id=room_id)
    
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')  # Redirect to the booking list page

    return render(request, 'hotel/delete_booking.html', {'booking': booking})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'hotel/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'hotel/login.html', {'form': form})

# Logout View
def logout_view(request):
    #if request.method == 'POST':
        logout(request)
        messages.success(request,"You have logged out successfully")
        return redirect('login')

# User Profile View
@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'hotel/profile.html', {'u_form': u_form})

