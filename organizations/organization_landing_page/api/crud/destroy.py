from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_landing_page.serializers.crud.crud import OrganizationLandingPageCrudSerializer

class OrganizationLandingPageDestroyApiView(generics.DestroyAPIView):
    queryset = OrganizationLandingPage.objects.all()
    serializer_class = OrganizationLandingPageCrudSerializer
