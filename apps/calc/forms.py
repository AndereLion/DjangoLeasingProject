from django import forms
from .models import CarRequest


# class ReviewForm(forms.Form):
#     car_brand = forms.CharField(label="Car Brand", max_length=50)
#     car_model = forms.CharField(label="Car Model", max_length=50)
#     car_year = forms.IntegerField(label="Car Year", max_value=2022, min_value=2011)
#     car_firs_payment = forms.IntegerField(label="First Payment", min_value=35000)
#     comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={'class': 'text_area'}))

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


