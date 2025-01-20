from rest_framework.generics import UpdateAPIView
from organizations.models.organization_user import OrganizationUser
from organizations.organization_user.serializers.crud.crud import OrganizationUserCreateUpdateSerializer


class OrganizationUserUpdateView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserCreateUpdateSerializer
