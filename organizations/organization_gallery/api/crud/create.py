from rest_framework.generics import CreateAPIView

from organizations.models import OrganizationGallery
from organizations.organization_gallery.serializers.crud.crud import OrganizationGalleryCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationGalleryCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationGallery.objects.all()
    serializer_class = OrganizationGalleryCreateUpdateSerializer
