from django.db.models.signals import post_migrate
from django.dispatch import receiver
from organization.utils.universities.university_degre import degrees
from organization.utils.universities.faculties import list
from organization.models.models import OrganizationType, OrganizationDegrees
from organization.models.organization_fields import OrganizationFields

types = [
    {
        'name': 'Maktab'
    },
    {
        'name': "O'quv markaz"
    },
    {
        'name': "Universitet"
    },
    {
        'name': "Kollej"
    },
    {
        "name": "Texnikum"
    },
    {
        'name': 'Litsey'
    }
]


@receiver(post_migrate)
def create_dates(sender, **kwargs):
    universitet = OrganizationType.objects.get(name='Universitet')
    for i in types:
        OrganizationType.objects.get_or_create(name=i['name'])
    for i in degrees:
        OrganizationDegrees.objects.get_or_create(name=i['name'], organization_type=universitet)
    for i in list:
        OrganizationFields.objects.get_or_create(name=i['name'], organization_type=universitet)
