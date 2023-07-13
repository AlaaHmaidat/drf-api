from django.shortcuts import render
from rest_framework import generics
from .models import Thing
from .serializers import Thingserializer
# Create your views here.

# ListAPIView
class Thing_list(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = Thingserializer

# RetrieveAPIView
class Thing_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = Thingserializer