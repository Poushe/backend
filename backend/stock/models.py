from django.db import models
import uuid

# Create your models here.
class income(models.Model):
    name=models.CharField(max_length=200, blank=True, null=True)
    In_amount=models.DecimalField(max_digits=8, decimal_places=2)
    In_date=models.DateField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name
    
class expense(models.Model):
    name=models.CharField(max_length=200, blank=True, null=True)
    Ex_amount=models.DecimalField(max_digits=8, decimal_places=2)
    Ex_date=models.DateField(auto_now=True,null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name
