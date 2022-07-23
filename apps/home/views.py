from django.shortcuts import render

from apps.home.models import CarInStock


def home_view(request):
    car_in_sock = CarInStock.objects.all()
    return render(request, 'home/home.html', context={'car_in_sock': car_in_sock})
