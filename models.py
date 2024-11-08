from django.db import models
from django.contrib.auth.models import User

   # Room Model
class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    description = models.TextField(default="description")
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
        

    def __str__(self):
        return f"Room {self.room_number} {{self.room_type.name}}"

   # Booking Model
class Booking(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()


    def __str__(self):
        return f"Booking by {self.name}-{self.room} ({self.check_in} to {self.check_out})"