
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



    