from django import forms


class ReviewForm(forms.Form):
    car_brand = forms.CharField(label="Car Brand", max_length=50)
    car_model = forms.CharField(label="Car Model", max_length=50)
    car_year = forms.IntegerField(label="Car Year")
    car_firs_payment = forms.CharField(label="First Payment", max_length=10)
