from django.core import validators
from django import forms
from .models import Students

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['First_name', 'Last_name', 'attendance']
        #agree= forms.BooleanField( label_suffix='', label='I agree')