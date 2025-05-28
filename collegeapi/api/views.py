from django.shortcuts import render
from rest_framework import  viewsets
from api.models import College
from api.serailzers import CollegeSerializer


# Create your views here.
class CollegeViewset(viewsets.ModelViewSet):
  queryset=College.objects.all()
  serializer_class = CollegeSerializer

  