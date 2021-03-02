from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(blank=True, max_length=100)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    subscriber = models.ForeignKey(
        User, related_name='subscribers',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.subscriber


class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)
    description = models.TextField()
    price = models.IntegerField()
    title = models.CharField(blank=True, max_length=200)
    add_date = models.DateTimeField("add date", auto_now_add=True)
    product_view = models.IntegerField(default=0)

    def __str__(self):
        return self.name

