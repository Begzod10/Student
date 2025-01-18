from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from organizations.models.models import OrganizationDegrees
from organizations.organization_degree.serializers.crud.crud import OrganizationDegreesCreateUpdateSerializer


class OrganizationDegreesDeleteView(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationDegrees.objects.all()
    serializer_class = OrganizationDegreesCreateUpdateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({"message": "OrganizationDegrees deleted successfully."}, status=status.HTTP_200_OK)
