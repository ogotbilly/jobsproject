from django import forms
from django.core.validators import RegexValidator
from messaging.models import Message

class MessageForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r"(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})", message="invalid phone number format, required format +254727750213")
    phone_number = forms.CharField(validators=[phone_regex],help_text="Enter phone number in format +254",max_length=13, required=True)
    message      = forms.CharField(help_text="Type the message you want to send to the parent",initial="Enter the text message you wish to send, in the widget", required=True,widget=forms.Textarea())


    class Meta:
        model = Message
        fields = ['phone_number', 'message']