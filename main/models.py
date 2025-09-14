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
    
    GENDER_CHOICES = [('female', 'Female'),
                      ('male', 'Male'),
                      ('unisex', 'Unisex')]

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
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Unisex")
    product_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.product_views > 20
    
    def increment_views(self):
        self.product_views += 1
        self.save()