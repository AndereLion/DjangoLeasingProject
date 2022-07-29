from django.db import models
from django.core.validators import validate_email, MaxValueValidator, MinValueValidator, MinLengthValidator, \
    MaxLengthValidator


# Create your models here.

class CarRequest(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField(validators=[MinValueValidator(2011), MaxValueValidator(2022)])
    car_first_payment = models.IntegerField(validators=[MinValueValidator(1000)])
    phone_number = models.CharField(max_length=20, validators=[MinLengthValidator(9), MaxLengthValidator(13)])
    email = models.EmailField(validators=[validate_email])
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Brand: {self.car_brand}, Model: {self.car_model}, Year: {self.car_year}, ' \
               f'First payment: {self.car_first_payment}'
