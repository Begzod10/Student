from rest_framework import generics
from organizations.models import OrganizationUser
from organizations.organization_user.serializers.get.retrieve_view import OrganizationUserSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationUserDetailView(generics.RetrieveAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer
    lookup_field = 'pk'
