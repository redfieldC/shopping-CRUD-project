from tkinter import CASCADE
from django.db import models
from categories.models import Categories
from sub_categories.models import SUBCategories
from colors.models import Colors
from Size.models import Size
# Create your models here.
class Products(models.Model):
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    sub_categories = models.ForeignKey(SUBCategories,on_delete=models.CASCADE)
    color = models.ForeignKey(Colors,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    # image = models.ImageField(upload_to = 'media/',width_field=None,height_field=None,null=True)
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    sku_number = models.CharField(max_length=10)
    product_details = models.CharField(max_length=300)
    quantity = models.IntegerField(default=0)
    isactive = models.BooleanField(default=True)
    