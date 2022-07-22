from django.urls import path
from .views import calc_view, thank_you_view

app_name = 'calc'
urlpatterns = [

    path('', calc_view, name='calc_view'),
    path('thank_you/', thank_you_view, name='thank_you')

]
