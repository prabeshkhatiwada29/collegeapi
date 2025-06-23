from django.contrib import admin
from api.models import College, student, staff, Faculty

class CustomBaseAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("css/admin_custom.css",)}
        js = ("js/admin_custom.js",)

class CollegeAdmin(CustomBaseAdmin):
    list_display = ('name', 'location', 'established_year')
    search_fields = ('name', 'location', )

class StudentAdmin(CustomBaseAdmin):
    list_display = ('name', 'age', 'college', )
    search_fields = ('name', 'college__name', )
    list_filter = ('college', )

class StaffAdmin(CustomBaseAdmin):
    list_display = ('name', 'age', 'college', 'position')
    search_fields = ('name', 'college__name', 'position', )
    list_filter = ('college', 'position', )

class FacultyAdmin(CustomBaseAdmin):
    list_display = ('name', 'age', 'college', 'department')
    search_fields = ('name', 'college__name', 'department', )
    list_filter = ('college', 'department', )

admin.site.register(College, CollegeAdmin)
admin.site.register(student, StudentAdmin)
admin.site.register(staff, StaffAdmin)
admin.site.register(Faculty, FacultyAdmin)
