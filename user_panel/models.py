from itertools import product
from django.db import models

# Create your models here.

class products(models.Model):
    user_id = models.BigIntegerField()
    name = models.TextField()
    product_code = models.TextField()
    price = models.TextField()
    category = models.TextField()
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    updated_at = models.DateField()
    created_at = models.DateField()

