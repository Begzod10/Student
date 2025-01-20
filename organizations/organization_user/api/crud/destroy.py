from rest_framework import generics

from organizations.models.organization_user import OrganizationUser
from organizations.organization_user.serializers.crud.crud import OrganizationUserCreateUpdateSerializer


class OrganizationUserDestroyApiView(generics.DestroyAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserCreateUpdateSerializer
