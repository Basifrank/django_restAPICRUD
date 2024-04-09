#The serializer is used to convert data in the django db moodel into something that we can turn into json
from rest_framework import serializers

from .models import Task, Item, Location


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')
        

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')