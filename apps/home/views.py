from django.shortcuts import render

from apps.home.models import CarInStock
from .forms import OwnCalculatingForm


def calc_leasing(term, car_year, first_payment, car_price):
    percent = (2022 - car_year) * 2 + (term * 2)
    return round((((car_price - first_payment) / 100 * percent + (car_price - first_payment)) / term), 2)


def home_view(request, *args, **kwargs):
    car_in_sock = CarInStock.objects.all()
    if request.method == "POST":
        form = OwnCalculatingForm(request.POST)
        if form.is_valid():
            leasing_term = form.cleaned_data['leasing_term']
            car_year = form.cleaned_data['car_year']
            car_firs_payment = form.cleaned_data['car_firs_payment']
            car_price_in_market = form.cleaned_data['car_price_in_market']
            result = calc_leasing(leasing_term, car_year, car_firs_payment, car_price_in_market)
            return render(request, 'home/home.html',
                          context={'car_in_sock': car_in_sock, "form": form, "result": result})

    else:
        form = OwnCalculatingForm()

    return render(request, 'home/home.html', context={'car_in_sock': car_in_sock, "form": form})
