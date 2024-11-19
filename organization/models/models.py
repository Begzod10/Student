from django.db import models

from students.models.academic_year import AcademicYear
from students.models.region import Region
from students.models.student import Shift


class OrganizationType(models.Model):
    name = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organization_type/', null=True, blank=True)

    class Meta:
        app_label = 'organization'


class OrganizationDegrees(models.Model):
    name = models.CharField(max_length=250, null=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organization'


class Organization(models.Model):
    name = models.CharField(max_length=250, null=True)
    locations = models.CharField(max_length=250, null=True)
    desc = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='organization/', null=True, blank=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organization'


class File(models.Model):
    type = models.CharField()
    url = models.URLField()

    class Meta:
        app_label = 'organization'


class OrganizationGallery(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    organization_id = models.BigIntegerField()

    class Meta:
        app_label = 'organization'


class OrganizationLandingPage(models.Model):
    organization_id = models.ForeignKey("Organization", on_delete=models.CASCADE)
    year_id = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    desc = models.TextField()
    name_optional = models.CharField(null=True, blank=True)
    expire_date = models.DateField()
    degree_id = models.ForeignKey("OrganizationDegrees", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = 'organization'


class GrantShift(models.Model):
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE)
    duration = models.IntegerField()
    grant = models.ForeignKey('LandingPageGrant', on_delete=models.CASCADE)

    class Meta:
        app_label = 'organization'


class LandingPageGrant(models.Model):
    landing_page = models.ForeignKey('OrganizationLandingPage', on_delete=models.CASCADE)
    desc = models.TextField()

    class Meta:
        app_label = 'organization'


class OrganizationAdvantage(models.Model):
    name_optional = models.CharField(null=True, blank=True)
    desc = models.TextField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    class Meta:
        app_label = 'organization'


class GrantField(models.Model):
    field_id = models.ForeignKey('organization.OrganizationFields', on_delete=models.CASCADE)
    ball = models.IntegerField()
    desc_optional = models.TextField(null=True, blank=True)
    grant = models.ForeignKey(LandingPageGrant, on_delete=models.CASCADE)

    class Meta:
        app_label = 'organization'


class LandingPageShift(models.Model):
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    landing_page = models.ForeignKey('OrganizationLandingPage', on_delete=models.CASCADE)
    duration = models.IntegerField()

    class Meta:
        app_label = 'organization'


class OrganizationAdvantages(models.Model):
    name = models.CharField(max_length=250, null=True)
    desc = models.TextField()
    file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = 'organization'
