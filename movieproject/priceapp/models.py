from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    price=models.TextField()

    def __str__(self):
        return self.name