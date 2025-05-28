# create serealizers for the college and student models
from rest_framework import serializers
from api.models import College

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = College
        fields = "__all__"  # Use double dashes to include all fields

