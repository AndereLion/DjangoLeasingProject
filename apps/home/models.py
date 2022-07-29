from django.db import models
from django.core.validators import validate_email, MaxValueValidator, MinValueValidator, MinLengthValidator, \
    MaxLengthValidator


# Create your models here.
class CarInStock(models.Model):
    img = models.ImageField(upload_to='')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(validators=[MinValueValidator(2011), MaxValueValidator(2022)])
    first_payment = models.IntegerField(validators=[MinValueValidator(1000)])
    mileage = models.IntegerField()
    engine = models.CharField(max_length=50, null=True)
    type_of_fuel = models.CharField(max_length=50, null=True)
    type_of_gearbox = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}, ' \
               f'First payment: {self.first_payment}'


class ImagesCarPortfolio(models.Model):
    img = models.ImageField(upload_to='')
    car = models.ForeignKey(CarInStock, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Brand: {self.img}'
