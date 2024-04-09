from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Task, Item, Location
from .serializers import ItemSerializer, LocationSerializer, TaskSerializer

# Create your views here.

#Plan is to convert it into a Json RestFramework API response


#allow us to have functionality that django rest framework gives
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemlocation=location)
        return queryset
            


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
 
    
class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    
class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
 