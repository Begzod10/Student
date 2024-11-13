from django.db import models
from Students.models.region import Region


class OrganizationType(models.Model):
    name = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organization_type/', null=True, blank=True)


class OrganizationDegrees(models.Model):
    name = models.CharField(max_length=250, null=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)


class Organization(models.Model):
    name = models.CharField(max_length=250, null=True)
    locations = models.CharField(max_length=250, null=True)
    desc = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organization/', null=True, blank=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
