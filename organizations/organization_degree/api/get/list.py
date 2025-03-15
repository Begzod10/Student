from rest_framework import generics

from organizations.models.models import OrganizationDegrees
from organizations.organization_degree.serializers.get.retrieve_view import OrganizationDegreesRetrieveSerializer


class OrganizationDegreesList(generics.ListAPIView):
    queryset = OrganizationDegrees.objects.all()
    serializer_class = OrganizationDegreesRetrieveSerializer


class OrganizationDegreesListByOrganizationType(generics.ListAPIView):
    queryset = OrganizationDegrees.objects.all()
    serializer_class = OrganizationDegreesRetrieveSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return OrganizationDegrees.objects.none()

        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")
        return OrganizationDegrees.objects.filter(organization_type_id=pk, deleted=False).all().order_by('id')
