from rest_framework.generics import CreateAPIView

from organizations.models import OrganizationGallery
from organizations.organization_gallery.serializers.crud.crud import OrganizationGalleryCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from organizations.models.models import File
from organizations.organization_gallery.serializers.crud.crud import FileCreateUpdateSerializer


class OrganizationGalleryCreateView(CreateAPIView):
    queryset = OrganizationGallery.objects.all()
    serializer_class = OrganizationGalleryCreateUpdateSerializer


class OrganizationGalleryFileCreateView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileCreateUpdateSerializer
    parser_classes = [MultiPartParser, FormParser]
