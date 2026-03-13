from django.db import models

# Create your models here.
"""
A model represents the table blueprint. 
It gives us access ot a model manager that we will embrace to handle CRUD operations 

Each model will inherit from the models.Model class
"""
class Lake(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    size = models.FloatField()
    latitude=models.FloatField()
    longitude =models.FloatField()
    isSalty = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Ocean(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    size = models.FloatField()
    latitude=models.FloatField()
    longitude =models.FloatField()
    isSalty = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name