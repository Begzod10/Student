from django.db import models


class OrganizationFields(models.Model):
    name = models.CharField(max_length=250, null=True)
    desc = models.TextField()
    admin_status = models.BooleanField(default=False)
    organization_type = models.ForeignKey('Organization.OrganizationType', on_delete=models.SET_NULL, null=True)
