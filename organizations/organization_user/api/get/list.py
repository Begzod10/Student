from rest_framework import generics
from organizations.models import OrganizationUser
from organizations.organization_user.serializers.get.retrieve_view import OrganizationUserSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationUserListView(generics.ListAPIView):
    serializer_class = OrganizationUserSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return OrganizationUser.objects.none()
        pk = self.kwargs.get('organization_id')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")
        return OrganizationUser.objects.filter(organization_id=pk)
