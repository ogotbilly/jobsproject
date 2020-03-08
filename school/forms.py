from django import forms
from django.contrib.auth.models import User
from .models import School


class MyschoolUpdateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name','image']

    