from django.db import models
# Create your models here.
class Colors(models.Model):
    color_name = models.CharField(max_length=10)
    color_description = models.CharField(max_length=10)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.color_name
    
