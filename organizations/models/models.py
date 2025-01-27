from django.db import models

from students.models.region import Region


class OrganizationType(models.Model):
    name = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organization_type/', null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        app_label = 'organizations'


class OrganizationDegrees(models.Model):
    name = models.CharField(max_length=250, null=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        app_label = 'organizations'


class Organization(models.Model):
    name = models.CharField(max_length=250, null=True)
    locations = models.JSONField(max_length=250, null=True)
    desc = models.TextField(null=True)
    desc_json = models.JSONField(null=True, blank=True)
    phone = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organizations/', null=True, blank=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)
    grand_text = models.TextField(null=True, blank=True)
    grand_json = models.JSONField(null=True, blank=True)

    class Meta:
        app_label = 'organizations'


class File(models.Model):
    type = models.CharField(max_length=255)  # Add max_length for better validation
    url = models.FileField(upload_to='file/', null=True, blank=True)  # FileField for handling file uploads

    class Meta:
        app_label = 'organizations'


class OrganizationGallery(models.Model):
    file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organizations'
