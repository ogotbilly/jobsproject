from django import forms
from .models import Pre_primary_1_attendance, Lower_primary_attendance, Upper_primary_attendance


class PrePrimaryOneAttendanceForm(forms.ModelForm):
    Monday = forms.BooleanField(required=False,initial=False,label='monday')
    Tuesday = forms.BooleanField(required=False,initial=False,label='tuesday')
    Wednessday = forms.BooleanField(required=False,initial=False,label='wednessday')
    Thursday = forms.BooleanField(required=False,initial=False,label='thursday')
    Friday = forms.BooleanField(required=False,initial=False,label='friday')
                                      
                                    
    class Meta:
        model = Lower_primary_attendance
        fields = ['Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday']

class LowerPrimaryOneAttendanceForm(forms.ModelForm):
    Monday = forms.BooleanField(required=False,initial=False,label='monday')
    Tuesday = forms.BooleanField(required=False,initial=False,label='tuesday')
    Wednessday = forms.BooleanField(required=False,initial=False,label='wednessday')
    Thursday = forms.BooleanField(required=False,initial=False,label='thursday')
    Friday = forms.BooleanField(required=False,initial=False,label='friday')
                                      
                                    
    class Meta:
        model = Lower_primary_attendance
        fields = ['Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday']

class UpperPrimaryOneAttendanceForm(forms.ModelForm):
    Monday = forms.BooleanField(required=False,initial=False,label='monday')
    Tuesday = forms.BooleanField(required=False,initial=False,label='tuesday')
    Wednessday = forms.BooleanField(required=False,initial=False,label='wednessday')
    Thursday = forms.BooleanField(required=False,initial=False,label='thursday')
    Friday = forms.BooleanField(required=False,initial=False,label='friday')
                                      
                                    
    class Meta:
        model = Upper_primary_attendance
        fields = ['Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday']

