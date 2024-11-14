from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Users(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(max_length=255, choices=SEX_CHOICES)
    born_date = models.DateField()
    born_address = models.CharField(max_length=255)
    indefikatsiya_pin = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    passport_pdf1 = models.FileField(upload_to='passport/', null=True, blank=True)
    passport_pdf2 = models.FileField(upload_to='passport/', null=True, blank=True)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    phone_extra = models.CharField(max_length=255)
    passport_seria = models.CharField(max_length=255)
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
