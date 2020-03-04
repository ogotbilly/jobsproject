from django.db import models
from django.utils import timezone


class Message(models.Model):
    phone_number = models.CharField(max_length=50)
    message = models.TextField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number

class Mail(models.Model):
    email_address = models.EmailField(max_length=50)
    message = models.TextField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email_address
    