from django import forms
from apps.admin_panel.models import CarInStock


class CarInStockForm(forms.ModelForm):
    class Meta:
        model = CarInStock
        fields = ['img', 'brand', 'model', 'year', 'first_payment', 'mileage', 'engine', 'type_of_fuel',
                  'type_of_gearbox']
        labels = {
            'img': "Images",
            'brand': "Brand",
            'model': "Model",
            'year': "Year",
            'first_payment': "First payment"
        }
