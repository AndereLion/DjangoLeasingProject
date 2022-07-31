from django.urls import path
from .views import details_view, photo_in_portfolio_delete_view

app_name = 'details'
urlpatterns = [

    path('<int:pk>/', details_view, name='details'),
    path('photo_in_portfolio_delete/<int:pk>/<int:pk_car>/', photo_in_portfolio_delete_view,
         name='photo_in_portfolio_delete')

]
