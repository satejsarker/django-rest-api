from django.shortcuts import render
from rest_framework import generics
from casionoFinder.models import Casino
from casionoFinder.serializer import CasinoSerializer
class ListCreateCasino(generics.ListCreateAPIView):
    queryset=Casino.objects.all()
    serializer_class=CasinoSerializer
