from django import forms
from .models import Customer, Product
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    age = forms.IntegerField()

    class Meta:
        model = Customer
        fields = ["name", "last_name", "email"]

    def clean_age(self):
        if self.cleaned_data['age'] < 18:
            raise ValidationError('Age must be at least 18.')
        return self.cleaned_data['age']


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

