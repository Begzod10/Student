from django.db import models

from education.models import EducationLanguage
from organizations.models.models import File
from students.models.academic_year import AcademicYear
from students.models.student import Shift


class OrganizationLandingPage(models.Model):
    organization = models.ForeignKey("Organization",related_name='organizationlandingpage', on_delete=models.CASCADE)
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=True)
    desc = models.TextField()
    expire_date = models.DateField()
    start_date = models.DateField(null=True)
    degree = models.ForeignKey("OrganizationDegrees", on_delete=models.SET_NULL, null=True, blank=True)
    education_language = models.ManyToManyField("education.EducationLanguage", blank=True)
    deleted = models.BooleanField(default=False)
    grant = models.BooleanField(default=False)
    price = models.BigIntegerField(null=True)
    requirements = models.TextField(null=True, blank=True)

    # CHANGED: Shift and Field to ManyToMany
    shift = models.ManyToManyField('students.Shift', blank=True)
    field = models.ForeignKey("organizations.OrganizationFields", blank=True, on_delete=models.SET_NULL, null=True)

    desc_json = models.JSONField(null=True, blank=True)
    requirements_json = models.JSONField(null=True, blank=True)

    class Meta:
        app_label = 'organizations'


class OrganizationAdvantage(models.Model):
    name_optional = models.CharField(null=True, blank=True)
    desc = models.TextField()
    desc_json = models.JSONField(null=True, blank=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'organizations'
