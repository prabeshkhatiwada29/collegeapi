from django.contrib import admin
from django.urls import path
from api.views import CollegeViewset
from rest_framework import routers
from django.urls import include


router=routers.DefaultRouter()
router.register(r'colleges', CollegeViewset)


urlpatterns = [
   path("",include(router.urls))

  
]
