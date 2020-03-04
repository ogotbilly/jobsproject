from django.urls import path
from messaging import views

urlpatterns = [
    path('home/send-messages', views.message, name='send-message'),
    path('home/send-email', views.email, name='send-email'),
]
