# create serealizers for the college and student models
from rest_framework import serializers
from api.models import College, student, staff

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = College
        fields = "__all__"  # Use double dashes to include all fields

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = student
        fields = "__all__"

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = staff
        fields = "__all__"  # Assuming staff is also a student model, adjust as necessary
