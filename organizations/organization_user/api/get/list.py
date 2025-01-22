from rest_framework import generics
from organizations.models import OrganizationUser
from organizations.organization_user.serializers.get.retrieve_view import OrganizationUserSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationUserListView(generics.ListAPIView):
    serializer_class = OrganizationUserSerializer

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return OrganizationUser.objects.filter(organization_id=organization_id)
