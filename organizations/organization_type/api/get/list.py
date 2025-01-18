from organizations.models.models import OrganizationType


from rest_framework import generics
from organizations.organization_type.serializers.get.list import OrganizationTypeSerializerList


class OrganizationTypeListView(generics.ListAPIView):
    queryset = OrganizationType.objects.filter(deleted=False).all()
    serializer_class = OrganizationTypeSerializerList