from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from organizations.models.organization_user import OrganizationUser
from organizations.organization_user.serializers.crud.crud import OrganizationUserCreateUpdateSerializer


class OrganizationUserDestroyApiView(generics.DestroyAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserCreateUpdateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.delete()
        instance.delete()
        return Response({"message": "OrganizationUser and associated user deleted successfully."},
                        status=status.HTTP_200_OK)
