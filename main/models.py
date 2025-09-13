import uuid
from django.db import models

# Create your models here.


class Product(models.Model):

    CATEGORY_CHOICES = [('shoes', 'Shoes'),
                        ('jersey', 'Jersey'),
                        ('shorts', 'Shorts'),
                        ('jacket', 'Jacket'),
                        ('accessory', 'Accessory'),
                        ('ball', 'Ball'),
                        ('exclusive', 'Exclusive'),] 

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    bonus_points = models.IntegerField(default=0)
    brand = models.CharField(max_length=255, default="Unknown")

    def __str__(self):
        return self.title