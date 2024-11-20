from django.db import models


class OrganizationFields(models.Model):
    name = models.CharField(max_length=250, null=True)
    desc = models.TextField()
    admin_status = models.BooleanField(default=False)
    organization_type = models.ForeignKey('organizations.OrganizationType', on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organizations'
