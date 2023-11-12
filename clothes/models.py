from django.db import models


class CustomerCl(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class TagCl(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductCl(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(TagCl)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class OrderCl(models.Model):
    customer_name = models.CharField(default='Without_Name', max_length=100)
    products = models.ManyToManyField(ProductCl)
    order_date = models.DateField(auto_now_add=True)
