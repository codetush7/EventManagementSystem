
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Event(models.Model):
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('corporate', 'Corporate Event'),
        ('anniversary', 'Anniversary'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    event_date = models.DateField()
    venue = models.CharField(max_length=255)
    guests = models.PositiveIntegerField()
    instructions = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type.title()} on {self.event_date} for {self.customer.username}"

    