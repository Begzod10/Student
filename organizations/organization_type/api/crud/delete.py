from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from organizations.models.models import OrganizationType
from organizations.organization_type.serializers.crud.create import OrganizationTypeCreateSerializer


class DeleteOrganizationTypeView(generics.DestroyAPIView):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeCreateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({"message": "OrganizationType deleted successfully."}, status=status.HTTP_200_OK)
