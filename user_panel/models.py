from django.db import models
from datetime import datetime

# Create your models here.

def return_date_time():
    now = datetime.now()
    return now

class products(models.Model):
    user_id = models.BigIntegerField()
    name = models.TextField()
    product_code = models.TextField()
    price = models.TextField()
    category = models.TextField()
    manufacturing_date = models.DateField(default=return_date_time())
    expiry_date = models.DateField(default=return_date_time())
    updated_at = models.DateField(default=return_date_time())
    created_at = models.DateField(default=return_date_time())
    def __str__(self):
        return self.name
    

class users(models.Model):
    email = models.TextField()
    password = models.TextField()
    def __str__(self):
        return self.email