from typing import Any
from django import forms
from .models import Booking
from .models import Room
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','room', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        
        if room and check_in and check_out:
            conflicting_bookings = Booking.objects.filter(
                room = room,
                check_in__lt = check_out,
                check_out__gt = check_in
            )

            if conflicting_bookings.exists():
                raise ValidationError(
                    _('This room is already booked for the selected dates.'),
                    code='invalid'
                )
        return cleaned_data    

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number','price_per_night', 'description', 'room_type', 'is_available']


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']