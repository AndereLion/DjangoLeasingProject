from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def user_login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('home:home')
        except:

            print('User or password is incorrect')

    return render(request, 'user/login_page.html')


def logout_user(request):
    logout(request)
    return redirect('/user/login')
