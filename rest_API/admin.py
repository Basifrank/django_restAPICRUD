from django.contrib import admin

from .models import Task, Location, Item

# Register your models here.
admin.site.register(Task)
admin.site.register(Location)
admin.site.register(Item)