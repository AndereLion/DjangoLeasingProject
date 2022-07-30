from django.urls import path
from .views import admin_panel_view, car_added_view, car_delete_view

app_name = 'admin_panel'
urlpatterns = [

    path('', admin_panel_view, name='admin_panel'),
    path('car_added/', car_added_view, name='car_added'),
    path('car_delete/<int:pk>', car_delete_view, name='car_delete')
]
