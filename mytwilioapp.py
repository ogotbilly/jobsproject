# from django.http import HttpResponse  
# from django.shortcuts import render  
# from django.contrib.sites.shortcuts import get_current_site  
# from django.utils.encoding import force_bytes, force_text  
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
# from django.template.loader import render_to_stringfrom .forms import SignUpForm  
# from .tokens import account_activation_token  
# from django.contrib.auth.models import User  
# from django.core.mail import EmailMessagedef signup(request):  
#         if request.method == 'GET':  
#             return render(request, 'accounts/signup.html')  
#         if request.method == 'POST':  
#             form = SignUpForm(request.POST)  
#             # print(form.errors.as_data())  
#             if form.is_valid():  
#                 user = form.save(commit=False)  
#                 user.is_active = False  
#                 user.save()  
#                 current_site = get_current_site(request)  
#                 mail_subject = 'Activate your account.'  
#                 message = render_to_string('accounts/acc_active_email.html', {  
#                     'user': user,  
#                     'domain': current_site.domain,  
#                     'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),  
#                     'token': account_activation_token.make_token(user),  
#                 })  
#                 to_email = form.cleaned_data.get('email')  
#                 email = EmailMessage(  
#                     mail_subject, message, to=[to_email]  
#                 )  
#                 email.send()  
#                 return HttpResponse('Please confirm your email address to complete the registration')  
#          else:  
#             form = SignUpForm()  
#          return render(request, 'accounts/signup.html', {'form': form})def activate(request, uidb64, token):  
#         try:  
#             uid = force_text(urlsafe_base64_decode(uidb64))  
#             user = User.objects.get(id=uid)  
#         except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
#             user = None  
#         if user is not None and account_activation_token.check_token(user, token):  
#             user.is_active = True  
#             user.save()  
#             return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
#         else:  
#             return HttpResponse('Activation link is invalid!')

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8e1778c523a5cddecd65cea189f83231'
auth_token = '3f24ff5b064e0f32a261b6d4efcb22eb'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hello mr felix, you current",
                     from_='+12248033141',
                     to='+254711213592'
                 )

connection_error = ['message']['-3']
if connection_error:
    print(message.json)





# safaricom test cridentials for B2C simulation transaction
# consumer_key = "z7GkV63JgMEMVZ0Utu9ThdAewxhGTidG"
# consumer_secret = "igyMj3nNcVRtX3yA"