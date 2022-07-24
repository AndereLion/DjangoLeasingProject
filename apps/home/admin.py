from django.contrib import admin

# Register your models here.
from apps.home.models import CarInStock, ImagesCarPortfolio

admin.site.register(CarInStock)
admin.site.register(ImagesCarPortfolio)
