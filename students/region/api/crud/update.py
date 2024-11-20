from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from students.models.region import Region
from students.region.serializers.get.retrieve_view import RegionSerializer


class RegionUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
