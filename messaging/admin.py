from django.contrib import admin
from .models import Message, TwilioMesaage



class AdminTwilioMessage(admin.ModelAdmin):
    list_display = ['Sent_to', 'Message_status', 'Price_unit', 'Message_sid']


admin.site.register(Message)
admin.site.register(TwilioMesaage, AdminTwilioMessage)


