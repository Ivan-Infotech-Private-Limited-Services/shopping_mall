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
