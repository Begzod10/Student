from rest_framework.generics import CreateAPIView

from organizations.models.organization_user import OrganizationUser
from organizations.organization_user.serializers.crud.crud import OrganizationUserCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationUserCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserCreateUpdateSerializer

