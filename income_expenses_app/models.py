from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)
    
    def __str__(self) ->str:
        return self.category
    

class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)    

    def __str__(self) -> str:
        return self.category