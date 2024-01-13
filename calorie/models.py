from django.db import models

# Create your models here.
class count(models.Model):
    food=models.CharField(max_length=100)
    value=models.IntegerField(default=0)
    
