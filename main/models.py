import uuid
from django.db import models

# Create your models here.


class Product(models.Model):

    CATEGORY_CHOICES = [('player', 'Player'),
                        ('coach', 'Coach'),
                        ('manager', 'Manager'),
                        ('family', 'Family')] 

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField()

    def __str__(self):
        return self.title