from django.db import models
from user.models import User
from order.models import ShopProduct

# Create your models here.


class Order(models.Model):

    created = models.DateField(auto_now_add=True)
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Order {self.id}'


class ShopProductOrder(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shopproduct = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
