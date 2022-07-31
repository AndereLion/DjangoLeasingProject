from django.shortcuts import render, redirect

# Create your views here.
from apps.admin_panel.forms import ImagesCarPortfolioForm
from apps.admin_panel.models import CarInStock, ImagesCarPortfolio


def details_view(request, *args, **kwargs):
    car = CarInStock.objects.get(pk=kwargs['pk'])
    car_portfolio = ImagesCarPortfolio.objects.filter(car_id=kwargs['pk'])

    if request.method == "POST":
        form = ImagesCarPortfolioForm(request.POST, request.FILES, )

        if form.is_valid():
            form.save()

            return render(request, 'details/details.html',
                          context={"car": car, "car_portfolio": car_portfolio, "form": form})

    else:
        form = ImagesCarPortfolioForm()

    return render(request, 'details/details.html', context={"car": car, "car_portfolio": car_portfolio, "form": form})


def photo_in_portfolio_delete_view(request, *args, **kwargs):
    ImagesCarPortfolio.objects.get(pk=kwargs['pk']).delete()
    return redirect('details:details', kwargs['pk_car'])
