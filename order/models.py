from django.db import models
from user.models import User
from prod_and_cat.models import ShopProduct

# Create your models here.
from core.models import BaseModel


class Order(BaseModel):


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Order {self.id}"


class ShopProductOrder(BaseModel):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shopproduct = models.ForeignKey(
        "prod_and_cat.ShopProduct", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.id
