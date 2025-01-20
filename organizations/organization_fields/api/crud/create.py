from rest_framework import generics

from ...serializers.crud.serializers import OrganizationFieldsListSerializersUpdate, OrganizationFields


class OrganizationFieldsCreate(generics.CreateAPIView):
    queryset = OrganizationFields.objects.all()
    serializer_class = OrganizationFieldsListSerializersUpdate
