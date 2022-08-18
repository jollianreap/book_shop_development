from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    author_name = models.CharField(max_length=64, unique=False, blank=False)
    product_name = models.CharField(verbose_name='Book`s name', null=False, max_length=50)
    description = models.TextField(verbose_name='Book`s description', null=False)
    price = models.PositiveIntegerField(verbose_name='Book`s price')
    # image = models.ImageField(upload_to='images', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Book`s quantity', default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):

        return self.product_name
