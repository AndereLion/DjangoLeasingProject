from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ReviewForm
from .models import CarRequest


def calc_view(request, *args, **kwargs):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            #
            # # CarRequest.objects.create({
            # #     "car_brand": "Audi",
            # #     "car_model": "A3",
            # #     "car_year": 2015,
            # #     "car_first_payment": 36000
            # # })
            # new_car_request = CarRequest()
            # new_car_request.car_year = form.cleaned_data['car_year']
            # new_car_request.car_model = form.cleaned_data['car_model']
            # new_car_request.car_brand = form.cleaned_data['car_brand']
            # new_car_request.car_firs_payment = form.cleaned_data['car_firs_payment']
            # new_car_request.comment = form.cleaned_data['comment']
            # new_car_request.save()
            return redirect(reverse('calc:thank_you', ))
            # return render(request, 'calc/thank_you.html', context={"form_data": form.cleaned_data})
    else:
        form = ReviewForm()
    return render(request, 'calc/calc.html', context={"form": form})


def thank_you_view(request, *args, **kwargs):
    return render(request, 'calc/thank_you.html')
