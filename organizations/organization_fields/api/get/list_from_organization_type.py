from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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
        return OrganizationFields.objects.filter(organization_type_id=pk, deleted=False).all().order_by('name')


class OrganizationFields2ListView(APIView):
    def get(self, request, pk=None):
        if getattr(self, 'swagger_fake_view', False):
            return Response([], status=status.HTTP_200_OK)

        if pk is None:
            return Response({'detail': "'pk' not found in URL kwargs."}, status=status.HTTP_400_BAD_REQUEST)

        fields = OrganizationFields.objects.filter(
            organization_type_id=pk,
            deleted=False
        ).order_by('id')
        serializer = OrganizationFieldsListSerializers(fields, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
