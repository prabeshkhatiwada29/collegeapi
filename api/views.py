from django.shortcuts import render
from rest_framework import  viewsets
from api.models import College, student, staff , Faculty
from api.serailzers import CollegeSerializer, StudentSerializer, StaffSerializer, FacultySerializer
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.
class CollegeViewset(viewsets.ModelViewSet):
  queryset=College.objects.all()
  serializer_class = CollegeSerializer

  @action(detail=True, methods=['get'])
  def students(self,request, pk=None):
    try:
      College=College.objects.get(pk=pk)
      students = student.objects.filter(college=College)
      student_serailizer = StudentSerializer(students, many=True)
      return Response(student_serailizer.data)
    except Exception as e:
      return Response({"error": str(e)}, status=400)
    



class StudentViewset(viewsets.ModelViewSet):
  queryset = student.objects.all()
  serializer_class = StudentSerializer


class StaffViewset(viewsets.ModelViewSet):
  queryset = staff.objects.all()
  serializer_class = StaffSerializer


class FacultyViewset(viewsets.ModelViewSet):
  queryset = Faculty.objects.all()
  serializer_class = FacultySerializer

  @action(detail=True, methods=['get'])
  def students(self, request, pk=None):
    try:
      faculty_member = Faculty.objects.get(pk=pk)
      students = student.objects.filter(faculty=faculty_member)
      student_serializer = StudentSerializer(students, many=True)
      return Response(student_serializer.data)
    except Exception as e:
      return Response({"error": str(e)}, status=400)
 
  