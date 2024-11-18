from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Users(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)

    last_name = models.CharField(max_length=255, null=True)
    SEX_CHOICES = (
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol'),
    )
    sex = models.CharField(max_length=255, choices=SEX_CHOICES, null=True)
    born_date = models.DateField(null=True)
    born_address = models.CharField(max_length=255, null=True)
    indefikatsiya_pin = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True,unique=True)
    passport_pdf1 = models.FileField(upload_to='passport/', null=True, blank=True)
    passport_pdf2 = models.FileField(upload_to='passport/', null=True, blank=True)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='user')
    email = models.EmailField(unique=True,null=True)
    phone_extra = models.CharField(max_length=255, null=True)
    passport_seria = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = 'phone'

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True
    )

    class Meta:
        app_label = 'users'
