from django import forms
from .models import *


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "last_name", "email"]

