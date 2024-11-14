from django.db import models


class OrganizationUser(models.Model):
    job = models.ForeignKey('Organization.Jobs', on_delete=models.SET_NULL, null=True)
    organization_type = models.ForeignKey('Organization.OrganizationType', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('Users.Users', on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey('Organization.Organization', on_delete=models.SET_NULL, null=True)

