from django.contrib import admin
from .models import Jobs, OrganizationType, OrganizationDegrees, Organization, File, OrganizationGallery, OrganizationFields, OrganizationLandingPage, OrganizationAdvantage, OrganizationUser

# Register your models here.

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'deleted']
    list_filter = ['deleted']

@admin.register(OrganizationDegrees)
class OrganizationDegreesAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization_type', 'deleted']
    list_filter = ['deleted']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'region', 'organization_type', 'deleted']
    list_filter = ['deleted', 'organization_type', 'region']
    search_fields = ['name']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['type', 'url']

@admin.register(OrganizationGallery)
class OrganizationGalleryAdmin(admin.ModelAdmin):
    list_display = ['file', 'organization']

@admin.register(OrganizationFields)
class OrganizationFieldsAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_status', 'deleted']
    list_filter = ['admin_status', 'deleted']

@admin.register(OrganizationLandingPage)
class OrganizationLandingPageAdmin(admin.ModelAdmin):
    list_display = ['organization', 'year', 'expire_date', 'start_date', 'degree', 'education_language', 'deleted', 'grant', 'price']
    list_filter = ['deleted', 'grant', 'year']

@admin.register(OrganizationAdvantage)
class OrganizationAdvantageAdmin(admin.ModelAdmin):
    list_display = ['name_optional', 'organization', 'file']

@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    list_display = ['job', 'user', 'organization']
    list_filter = ['job', 'organization']
