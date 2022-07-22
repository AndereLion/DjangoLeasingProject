from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.urls import reverse


def calc_view(request, *args, **kwargs):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # return redirect(reverse('calc:thank_you', ))
            return render(request, 'calc/thank_you.html', context={"form_data": form.cleaned_data})
    else:
        form = ReviewForm()
    return render(request, 'calc/calc.html', context={"form": form})


def thank_you_view(request, *args, **kwargs):
    return render(request, 'calc/thank_you.html')
