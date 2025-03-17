from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


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
    phone = models.CharField(max_length=255, null=True, unique=True)
    passport_pdf1 = models.FileField(upload_to='passport/', null=True, blank=True)
    passport_pdf2 = models.FileField(upload_to='passport/', null=True, blank=True)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('organization_admin', ' '),
    )
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='user')
    email = models.EmailField(unique=True, null=True)
    phone_extra = models.CharField(max_length=255, null=True)
    passport_seria = models.CharField(max_length=255, null=True)
    file = models.ForeignKey('organizations.File', on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD = 'phone'
    image = models.ImageField(upload_to='users/', null=True, blank=True)
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


@receiver(pre_save, sender=Users)
def sync_phone_username(sender, instance, **kwargs):
    if not instance.phone and not instance.username:
        raise ValidationError("Either phone or username must be provided.")

    if not instance.username and instance.phone:
        instance.username = instance.phone

    elif not instance.phone and instance.username:
        instance.phone = instance.username
    print(instance.phone, instance.username)
    if Users.objects.filter(phone=instance.phone).exclude(id=instance.id).exists():
        raise ValidationError("This phone number is already in use. Please use a different phone number.")
    if Users.objects.filter(username=instance.username).exclude(id=instance.id).exists():
        raise ValidationError("This username is already taken. Please choose another one.")
