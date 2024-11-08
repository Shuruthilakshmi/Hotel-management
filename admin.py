from django.contrib import admin
from .models import Room, Booking

# Custom admin for Room model
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_number', 'room_type')

# Custom admin for Booking model
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'check_in', 'check_out')
    list_filter = ('check_in', 'check_out')
    search_fields = ('user__username', 'room__room_number')

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
