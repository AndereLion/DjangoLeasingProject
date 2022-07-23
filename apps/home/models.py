from django.db import models
from django.core.validators import validate_email, MaxValueValidator, MinValueValidator, MinLengthValidator, \
    MaxLengthValidator


# Create your models here.
class CarInStock(models.Model):
    img = models.ImageField(upload_to='')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(validators=[MinValueValidator(2011), MaxValueValidator(2022)])
    first_payment = models.IntegerField(validators=[MinValueValidator(35000)])
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}, ' \
               f'First payment: {self.first_payment}'
