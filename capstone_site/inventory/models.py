from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Stock(models.Model):
    """Creates inventory item objects and stores them in the database.
    

Attributes:
inventory_items(Charfield):The names of inventory items.

Modules:
__str__(self): returns the string form of stock objects.
"""
    inventory_items = models.CharField(max_length=100)

    def __str__(self):
        return self.inventory_items
    
class Query(models.Model):
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    name = models.CharField(("Name"), max_length=50)
    email_address = models.EmailField(unique=False, null=True)
    date_created = models.DateTimeField(auto_now=True)