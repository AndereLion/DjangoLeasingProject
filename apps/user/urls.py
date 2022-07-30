from django.urls import path
from .views import user_login_view, logout_user, user_sign_up_view, user_created_view

app_name = 'user'
urlpatterns = [

    path('login/', user_login_view, name='user_login'),
    path('logout/', logout_user, name='user_logout'),
    path('sign_up/', user_sign_up_view, name='user_sign_up'),
    path('user_created/', user_created_view, name='user_created')

]
