from django.urls import path
from .views import user_login_view, logout_user

app_name = 'user'
urlpatterns = [

    path('login/', user_login_view, name='user_login'),
    path('logout/', logout_user, name='user_logout')

]
