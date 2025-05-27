import pprint

from rest_framework import generics

from organizations.models import Organization, OrganizationUser
from organizations.organization.serializers.crud.create import OrganizationCreateSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status


class OrganizationCreateApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrganizationCreateSerializer
    queryset = Organization.objects.all()


class OrganizationDestroyApiView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrganizationCreateSerializer
    queryset = Organization.objects.all()

    def delete(self, request, *args, **kwargs):
        organization_user = OrganizationUser.objects.filter(organization=self.get_object())
        organization_user.delete()
        super().delete(request, *args, **kwargs)
        return Response({"message": "Tashkilot muvaffaqiyatli o'chirildi"}, status=status.HTTP_200_OK)
