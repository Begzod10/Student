from rest_framework.generics import UpdateAPIView
from organizations.models import OrganizationGallery
from organizations.models import File
from organizations.organization_gallery.serializers.crud.crud import FileCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser


class OrganizationGalleryUpdateView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = File.objects.all()
    serializer_class = FileCreateUpdateSerializer
    parser_classes = [MultiPartParser, FormParser]
