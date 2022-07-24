from django.urls import path
from .views import details_view

app_name = 'details'
urlpatterns = [

    path('<int:pk>/', details_view, name='details'),

]
