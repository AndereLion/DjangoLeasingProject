from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm


def calc_view(request, *args, **kwargs):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('calc:thank_you', ))

    else:
        form = ReviewForm()
    return render(request, 'calc/calc.html', context={"form": form})


def thank_you_view(request, *args, **kwargs):
    return render(request, 'calc/thank_you.html')
