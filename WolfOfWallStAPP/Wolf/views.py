from django.shortcuts import render
from rest_framework import generics
from .serializers import WolfSerializer, WolfListSerializer
from .models import Wolf
# Create your views here.


class WolfCreateView(generics.CreateAPIView):
    serializer_class = WolfSerializer


class WolfListView(generics.ListAPIView):
    serializer_class = WolfListSerializer
    queryset = Wolf.objects.all()


class WolfDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WolfSerializer
    queryset = Wolf.objects.all()