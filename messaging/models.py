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

class TwilioMesaage(models.Model):

    Sent_to = models.CharField(max_length=14)
    Message_body = models.TextField(max_length=200)
    Message_status = models.CharField(max_length=50)
    Price_unit = models.CharField(max_length=50)
    Message_sid = models.CharField(max_length=100)
    

    def __str__(self):
        return self.Sent_to
    
  