from django.db import models


# Create your models here.
class CarRequest(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_firs_payment = models.IntegerField()
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Brand: {self.car_brand}, Model: {self.car_model}, Year: {self.car_year}, First payment: {self.car_firs_payment}'
