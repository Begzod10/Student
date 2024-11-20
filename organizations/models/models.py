from django.db import models

from students.models.academic_year import AcademicYear
from students.models.region import Region
from students.models.student import Shift


class OrganizationType(models.Model):
    name = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organization_type/', null=True, blank=True)

    class Meta:
        app_label = 'organizations'


class OrganizationDegrees(models.Model):
    name = models.CharField(max_length=250, null=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organizations'


class Organization(models.Model):
    name = models.CharField(max_length=250, null=True)
    locations = models.CharField(max_length=250, null=True)
    desc = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organizations/', null=True, blank=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organizations'


class File(models.Model):
    type = models.CharField()
    url = models.URLField()

    class Meta:
        app_label = 'organizations'


class OrganizationGallery(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    organization_id = models.BigIntegerField()

    class Meta:
        app_label = 'organizations'


class OrganizationAdvantages(models.Model):
    name = models.CharField(max_length=250, null=True)
    desc = models.TextField()
    file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = 'organizations'
