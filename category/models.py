from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    createdAt = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name