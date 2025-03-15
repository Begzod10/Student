from rest_framework import generics

from ...serializers.crud.serializers import OrganizationFieldsListSerializersUpdate, OrganizationFields


class OrganizationFieldsUpdate(generics.UpdateAPIView):
    queryset = OrganizationFields.objects.all()
    serializer_class = OrganizationFieldsListSerializersUpdate
