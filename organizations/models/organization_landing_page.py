from django.db import models

from students.models.academic_year import AcademicYear
from students.models.region import Region
from students.models.student import Shift
from organizations.models.models import File


class OrganizationLandingPage(models.Model):
    organization_id = models.ForeignKey("Organization", on_delete=models.CASCADE)
    year_id = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    desc = models.TextField()
    name_optional = models.CharField(null=True, blank=True)
    expire_date = models.DateField()
    degree_id = models.ForeignKey("OrganizationDegrees", on_delete=models.SET_NULL, null=True, blank=True)
    grant = models.BooleanField(default=False)

    class Meta:
        app_label = 'organizations'


class OrganizationAdvantage(models.Model):
    name_optional = models.CharField(null=True, blank=True)
    desc = models.TextField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    class Meta:
        app_label = 'organizations'


class GrantField(models.Model):
    field_id = models.ForeignKey('organizations.OrganizationFields', on_delete=models.CASCADE)
    ball = models.IntegerField()
    desc_optional = models.TextField(null=True, blank=True)
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE,default=None)
    duration = models.IntegerField(default=0)
    landing_page = models.ForeignKey(OrganizationLandingPage, on_delete=models.CASCADE, default=None)

    class Meta:
        app_label = 'organizations'


class LandingPageShift(models.Model):
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    landing_page = models.ForeignKey('OrganizationLandingPage', on_delete=models.CASCADE)
    duration = models.IntegerField()

    class Meta:
        app_label = 'organizations'
