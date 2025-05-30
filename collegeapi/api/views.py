from django.shortcuts import render
from rest_framework import  viewsets
from api.models import College,student
from api.serailzers import CollegeSerializer, StudentSerializer


# Create your views here.
class CollegeViewset(viewsets.ModelViewSet):
  queryset=College.objects.all()
  serializer_class = CollegeSerializer


class StudentViewset(viewsets.ModelViewSet):
  queryset = student.objects.all()
  serializer_class = StudentSerializer
  