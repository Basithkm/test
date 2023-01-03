from django import forms
from .models import Details
from django.core import validators

class UserRegistration(forms.ModelForm):
    class Meta:
        model=Details
        fields = ['name','image','description']