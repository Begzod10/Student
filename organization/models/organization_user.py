from django.db import models

from users.models import Users


class OrganizationUser(models.Model):
    job = models.ForeignKey('organization.Jobs', on_delete=models.SET_NULL, null=True)
    organization_type = models.ForeignKey('organization.OrganizationType', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey('organization.Organization', on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organization'
