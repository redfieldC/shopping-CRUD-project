from django.db import models


# Create your models here.
class Categories(models.Model):
    #made changes to category_name for null and blank
    category_name = models.CharField(max_length=20)
    category_description = models.CharField(max_length=20)
    isactive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.category_name