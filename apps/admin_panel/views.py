from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CarInStockForm
from .models import CarInStock


def car_added_view(request):
    return render(request, 'admin_panel/car_added.html')


def admin_panel_view(request, *args, **kwargs):
    if request.method == "POST":
        form = CarInStockForm(request.POST, request.FILES, )

        if form.is_valid():
            form.save()

            return render(request, 'admin_panel/car_added.html')

    else:
        form = CarInStockForm()
    return render(request, 'admin_panel/admin_panel.html', context={"form": form})


def car_delete_view(request, *args, **kwargs):
    CarInStock.objects.get(pk=kwargs['pk']).delete()
    return redirect('home:home')
