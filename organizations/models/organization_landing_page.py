from django.db import models

from education.models import EducationLanguage
from organizations.models.models import File
from students.models.academic_year import AcademicYear
from students.models.student import Shift


class OrganizationLandingPage(models.Model):
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE)
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    desc = models.TextField()
    expire_date = models.DateField()
    start_date = models.DateField(null=True)
    degree = models.ForeignKey("OrganizationDegrees", on_delete=models.SET_NULL, null=True, blank=True)
    education_language = models.ForeignKey(EducationLanguage, on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(default=False)
    grant = models.BooleanField(default=False)
    price = models.BigIntegerField(null=True)
    requirements = models.TextField(null=True, blank=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, blank=True)
    field = models.ForeignKey("organizations.OrganizationFields", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = 'organizations'


class OrganizationAdvantage(models.Model):
    name_optional = models.CharField(null=True, blank=True)
    desc = models.TextField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'organizations'


class GrantField(models.Model):
    field_id = models.ForeignKey('organizations.OrganizationFields', on_delete=models.CASCADE)
    ball = models.IntegerField()
    desc_optional = models.TextField(null=True, blank=True)
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE, default=None)
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
