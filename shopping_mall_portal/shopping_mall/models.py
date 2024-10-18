from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()

class Shop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner_name = models.CharField(max_length=70)
    shop_no = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField()

class Product(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey(Shop, on_delete= models.RESTRICT)
    category = models.ForeignKey(Category, on_delete= models.RESTRICT)
    brand_name = models.CharField(max_length= 50, null=True, blank=True)
    price = models.FloatField(null=True)
    discount_price = models.FloatField( blank=True, default=0)
    image_url = models.URLField(null=True)
    stock_count = models.IntegerField(null=True)
    variant = models.CharField(max_length=50, null=True)
