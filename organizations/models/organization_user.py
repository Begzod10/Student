from django.db import models

from users.models import Users


class OrganizationUser(models.Model):
    job = models.ForeignKey('organizations.Jobs', on_delete=models.SET_NULL, null=True)
    organization_type = models.ForeignKey('organizations.OrganizationType', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'organizations'
