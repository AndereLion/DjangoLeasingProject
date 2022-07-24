from django import forms


class OwnCalculatingForm(forms.Form):
    leasing_term = forms.IntegerField(label="Leasing term in (month)", min_value=6, max_value=36)
    car_year = forms.IntegerField(label="Car Year", max_value=2022, min_value=2011)
    car_firs_payment = forms.IntegerField(label="First Payment in $", min_value=1000)
    car_price_in_market = forms.IntegerField(label="Car price in market", min_value=5000, max_value=150000)
