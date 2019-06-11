from django.db import models

class ProductData(models.Model):
    product_number = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_cost = models.IntegerField()
    product_class = models.CharField(max_length=50)
    product_weight = models.IntegerField()
