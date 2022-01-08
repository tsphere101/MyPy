from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100,default = '')
    description = models.TextField(blank = True,null = True)
    price = models.DecimalField(decimal_places=2,max_digits=10000,default=0)
    summary = models.TextField(default ='Cool!')
    feature = models.BooleanField(default=False)


