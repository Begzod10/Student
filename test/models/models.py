from django.db import models
from organizations.models.organization_fields import OrganizationFields
from test.models.subject import Subject


class Test(models.Model):
    name = models.CharField(null=True, blank=True)
    field = models.ForeignKey(OrganizationFields, on_delete=models.CASCADE, related_name='blocks', null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.BigIntegerField(null=True, blank=True)
    is_mandatory = models.BooleanField(null=True, blank=True)
