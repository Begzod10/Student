from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users, Comments


class UsersAdmin(UserAdmin):
    model = Users
    list_display = ['email', 'phone', 'name', 'surname', 'sex', 'born_date', 'role']
    search_fields = ('email', 'phone', 'name', 'surname')
    readonly_fields = ('id', 'indefikatsiya_pin', 'passport_pdf1', 'passport_pdf2')

    fieldsets = (
        (None, {'fields': (
            'email', 'phone', 'username', 'name', 'surname', 'last_name', 'sex', 'born_date', 'born_address', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional Info',
         {'fields': ('indefikatsiya_pin', 'phone_extra', 'passport_seria', 'file', 'passport_pdf1', 'passport_pdf2')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2', 'role')}
         ),
    )

    ordering = ('email',)


class CommentsAdmin(admin.ModelAdmin):
    model = Comments
    list_display = ['user', 'comment', 'created_at', 'rating', 'organization', 'name', 'surname']


# Register your models here.
admin.site.register(Users, UsersAdmin)
