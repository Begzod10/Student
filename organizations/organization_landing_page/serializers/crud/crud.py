from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage


class OrganizationLandingPageSerializer(generics.RetrieveAPIView):
    model = OrganizationLandingPage
    fields = [
        'id',
        'organization',
        'year_id',
        'desc',
        'name_optional',
        'expire_date',
        'degree_id'
    ]
    depth = 1
