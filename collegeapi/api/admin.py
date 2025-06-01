from django.contrib import admin
from api.models import College, student


# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display= ('name', 'location', 'established_year')
    search_fields = ('name', 'location', )  

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'college', )
    search_fields = ('name', 'college__name', )  # Search by student name and college name
    list_filter = ('college', )  # Filter by college
admin.site.register(College,CollegeAdmin)
admin.site.register(student,StudentAdmin)
