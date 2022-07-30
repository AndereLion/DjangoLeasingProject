from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def user_login_view(request, *args, **kwargs):
    page = 'user_login'
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('home:home')
        except:
            messages.error(request, 'User or password is incorrect')
            print()

    return render(request, 'user/login_page.html')


def logout_user(request):
    logout(request)
    return redirect('user:user_login')


def user_sign_up_view(request):
    page = 'user_sign_up'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('user:user_created')

    context = {'page': page, 'form': form}

    return render(request, 'user/login_page.html', context)


def user_created_view(request):
    return render(request, 'user/user_created.html')
