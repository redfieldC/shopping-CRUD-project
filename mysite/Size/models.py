from django.db import models
# Create your models here.
class Size(models.Model):
    size_name = models.CharField(max_length=10)
    size_description = models.CharField(max_length=20)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.size_name
