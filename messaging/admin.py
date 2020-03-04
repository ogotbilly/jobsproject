from django.contrib import admin
from .models import Message, TwilioMesaage


admin.site.register(Message)
admin.site.register(TwilioMesaage)


class AdminTwilioMessage(admin.ModelAdmin):
    list_display = ['Sent_to', 'Message_status', 'Price_unit']
