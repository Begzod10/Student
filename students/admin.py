from django.contrib import admin

from .models import AcademicYear, Region, Shift, Student, StudentRequest


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('from_date', 'to')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization_type')
    list_filter = ('organization_type',)
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'certificate', 'region', 'education_name', 'education_type', 'education_address', 'education_region')
    search_fields = ('education_name', 'education_type', 'education_address')
    list_filter = ('region',)


@admin.register(StudentRequest)
class StudentRequestAdmin(admin.ModelAdmin):
    list_display = (
    'student', 'organization', 'shift', 'field', 'language', 'year', 'degree', 'landing_page', 'accepted')
    list_filter = ('organization', 'shift', 'language', 'year', 'degree', 'accepted', 'date')
    search_fields = ('student__user__username', 'organization__name')
    date_hierarchy = 'date'
