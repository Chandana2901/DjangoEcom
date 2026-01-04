from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    producer = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    