from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
from .forms import MessageForm, EmailForm
from school.models import Pre_primary, Lower_primary, Upper_primary
from .models import Message, TwilioMesaage



def message(request):

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # form.save()
            phone = form.cleaned_data.get("phone_number")
            message_data = form.cleaned_data.get("message")

           
            account_sid = 'AC8e1778c523a5cddecd65cea189f83231'
            auth_token = '3f24ff5b064e0f32a261b6d4efcb22eb'

            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                     body=message_data,
                     from_='+12248033141',
                     to=phone
                 )

            sent_to = message.to
            message_body = message.body
            message_status = message.status
            price_unit = message.price_unit
            message_sid = message.sid
            error_code = message.error_code
            error_message = message.error_message
            print(error_code)
           


            message_response = TwilioMesaage.objects.create(
                Sent_to = sent_to,
                Message_body = message_body,
                Message_status = message_status,
                Price_unit = price_unit,
                Message_sid = message_sid,
            )

            message_response.save()

            

            messages.success(request, f'message has been successfully sent to {phone}')
            return redirect("send-message")

           
    else:
        form = MessageForm()
    context = {
        "message": Pre_primary.objects.all(),
        "message_one": Lower_primary.objects.all(),
        "message_two": Upper_primary.objects.all(),
        "form": form
    }

    return render(request, 'messaging/send_message.html',context)


def email(request):

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid:
            form.save()
            mail = form.cleaned_data.get("email_address")
            email_message_data = form.cleaned_data.get("message")

            messages.success(request, f'Email has been successfully sent to {mail}')
            return redirect("send-email")
    else:
        form = EmailForm()

    return render(request, "messaging/send_email.html", {"form": form })





