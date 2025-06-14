from django.contrib import admin
from api.models import College, student,staff, Faculty


# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display= ('name', 'location', 'established_year')
    search_fields = ('name', 'location', )  

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'college', )
    search_fields = ('name', 'college__name', )  # Search by student name and college name
    list_filter = ('college', ) 
    
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'college', 'position')
    search_fields = ('name', 'college__name', 'position', )  # Search by staff name, college name, and position
    list_filter = ('college', 'position', )

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'college', 'department')
    search_fields = ('name', 'college__name', 'department', )  # Search by faculty name, college name, and department
    list_filter = ('college', 'department', )


admin.site.register(College,CollegeAdmin)
admin.site.register(student,StudentAdmin)
admin.site.register(staff,StaffAdmin)
admin.site.register(Faculty, FacultyAdmin)
