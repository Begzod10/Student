from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from ...serializers.crud.serializers import OrganizationFieldsListSerializersUpdate, OrganizationFields


class OrganizationFieldsDelete(generics.DestroyAPIView):
    queryset = OrganizationFields.objects.all()
    serializer_class = OrganizationFieldsListSerializersUpdate

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({"message": "OrganizationFields deleted successfully."}, status=status.HTTP_200_OK)
