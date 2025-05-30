from django.contrib import admin
from django.urls import path,include
from api.views import CollegeViewset, StudentViewset
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'colleges', CollegeViewset)
router.register(r'students', StudentViewset)


urlpatterns = [
   path("",include(router.urls))

  
]
