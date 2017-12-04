from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Character(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    race = models.CharField(null=True, max_length=30)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=30, default="default name")
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, default="default")
    damage = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    consumable = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def use_item(self, times):
        self.quantity -= times

    def __str__(self):
        return self.name + " (" + str(self.quantity) + ")"
