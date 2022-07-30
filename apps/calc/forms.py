from django import forms
from .models import CarRequest


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CarRequest
        fields = ['car_brand', 'car_model', 'car_year', 'car_first_payment', 'phone_number', 'email']
        labels = {
            'car_brand': "Brand",
            'car_model': 'Model',
            'car_year': 'Year',
            'car_first_payment': "First payment"
        }
