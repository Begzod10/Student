from rest_framework import generics

from ...serializers.get.list import OrganizationFieldsListSerializers, OrganizationFields


class OrganizationFieldsListView(generics.ListAPIView):
    queryset = OrganizationFields.objects.all()
    serializer_class = OrganizationFieldsListSerializers

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return OrganizationFields.objects.none()

        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")
        return OrganizationFields.objects.filter(organization_type_id=pk,deleted=False).all().order_by('id')
