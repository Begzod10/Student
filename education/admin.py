from django.contrib import admin

from .models import EducationLanguage


@admin.register(EducationLanguage)
class EducationLanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'img_display']
    search_fields = ['name']

    def img_display(self, obj):
        if obj.img:
            return "Image Uploaded"
        return "No Image"

    img_display.short_description = 'Image Status'
