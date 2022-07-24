from django.shortcuts import render

# Create your views here.
from apps.home.models import CarInStock, ImagesCarPortfolio


def details_view(request, *args, **kwargs):
    car = CarInStock.objects.get(pk=kwargs['pk'])
    car_portfolio = ImagesCarPortfolio.objects.filter(car_id=kwargs['pk'])
    return render(request, 'details/details.html', context={"car": car, "car_portfolio": car_portfolio})
