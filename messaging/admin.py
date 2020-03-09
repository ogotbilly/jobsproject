from django.contrib import admin
from .models import TwilioMesaage, Mail



class AdminTwilioMessage(admin.ModelAdmin):
    list_display = ['Sent_to', 'Message_status', 'Price_unit', 'Message_sid']


admin.site.register(Mail)
admin.site.register(TwilioMesaage, AdminTwilioMessage)


