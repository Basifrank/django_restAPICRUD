from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.locationName

class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.itemName