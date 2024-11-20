from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_landing_page.serializers.crud.crud import OrganizationLandingPageSerializer


class OrganizationLandingPageCreateView(generics.CreateAPIView):
    queryset = OrganizationLandingPage.objects.all()
    serializer_class = OrganizationLandingPageSerializer
