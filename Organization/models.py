from django.db import models

from Students.models.academic_year import AcademicYear
from Students.models.region import Region
from Students.models.student import Shift


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


class File(models.Model):
    type = models.CharField()
    url = models.URLField()


class OrganizationGallery(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    organization_id = models.BigIntegerField()


class OrganizationLandingPage(models.Model):
    organization_id = models.ForeignKey("Organization", on_delete=models.CASCADE)
    year_id = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    desc = models.TextField()
    name_optional = models.CharField(null=True, blank=True)
    expire_date = models.DateField()
    degree_id = models.ForeignKey("OrganizationDegrees", on_delete=models.SET_NULL, null=True, blank=True)


class GrantShift(models.Model):
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE)
    duration = models.IntegerField()
    grant = models.ForeignKey('LandingPageGrant', on_delete=models.CASCADE)


class LandingPageGrant(models.Model):
    landing_page = models.ForeignKey('OrganizationLandingPage', on_delete=models.CASCADE)
    desc = models.TextField()


class OrganizationAdvantage(models.Model):
    name_optional = models.CharField(null=True, blank=True)
    desc = models.TextField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)


class GrantField(models.Model):
    # field_id = models.ForeignKey('', on_delete=models.CASCADE)
    ball = models.IntegerField()
    desc_optional = models.TextField(null=True, blank=True)
    grant = models.ForeignKey(LandingPageGrant, on_delete=models.CASCADE)


class LandingPageShift(models.Model):
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    landing_page = models.ForeignKey('OrganizationLandingPage', on_delete=models.CASCADE)
    duration = models.IntegerField()
