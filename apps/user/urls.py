from django.urls import path
from .views import user_login_view

app_name = 'user'
urlpatterns = [

    path('login/', user_login_view, name='user_login'),

]
