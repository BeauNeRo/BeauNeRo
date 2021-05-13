from django.db import models
# from account.models import User

# Create your models here.

class Product(models.Model):
    key = models.IntegerField()
    name = models.CharField(max_length = 100)
    content = models.TextField()
    picture = models.TextField()
    
    def __str__(self):
        return self.name