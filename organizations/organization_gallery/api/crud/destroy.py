from rest_framework import generics

from organizations.models import OrganizationGallery
from organizations.organization_gallery.serializers.crud.crud import OrganizationGalleryCreateUpdateSerializer

from rest_framework.response import Response
from rest_framework import status


class OrganizationGalleryDestroyApiView(generics.DestroyAPIView):
    queryset = OrganizationGallery.objects.all()
    serializer_class = OrganizationGalleryCreateUpdateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "OrganizationGallery deleted successfully."}, status=status.HTTP_200_OK)
