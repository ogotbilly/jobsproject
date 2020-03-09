from django import forms
from django.core.validators import RegexValidator
from .models import TwilioMesaage, Mail

class MessageForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r"(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})", message="invalid phone number format, required format +254727750213")
    phone_number = forms.CharField(validators=[phone_regex],help_text="Enter phone number in format +254", initial="+254727750213" ,max_length=13, required=True)
    message      = forms.CharField(help_text="Type the message you want to send to the parent",initial="Enter the text message you wish to send, in the widget", required=True,widget=forms.Textarea())


    class Meta:
        model = TwilioMesaage
        fields = ['phone_number', 'message']


class EmailForm(forms.ModelForm):
    email_address = forms.EmailField(help_text="Enter email address in format abc@gmal.com", max_length=30, required=True)
    email_subject      = forms.CharField(help_text="Enter mail subject", required=True)
    message      = forms.CharField(help_text="Type the mail you want to send to the parent",initial="Enter the text message you wish to send, in the widget", required=True,widget=forms.Textarea())


    class Meta:
        model = Mail
        fields = ['email_address', 'email_subject', 'message']