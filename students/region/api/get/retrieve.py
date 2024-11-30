from rest_framework import generics

from students.models.region import Region
from students.region.serializers.get.retrieve_view import RegionSerializer


class RegionRetrieveView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
