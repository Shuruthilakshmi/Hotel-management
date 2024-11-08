from django.urls import path
from . import views 
from .views import signup_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',signup_view, name='signup'),
    path('room_list/', views.room_list, name='room_list'),

    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('book/', views.book_room, name='book_room'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('create/', views.create_room, name='create_room'),
    path('view/', views.view_rooms, name='view_rooms'),
    path('update/<int:room_id>/', views.update_room, name='update_room'),
    path('delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('cancel_booking/<int:room_id>/', views.cancel_booking, name='cancel_booking'),
    path('delete_booking/<int:room_id>/', views.delete_booking, name='delete_booking'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('booked-rooms/', views.booked_rooms, name='booked_rooms'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
  
  ]