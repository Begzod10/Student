from rest_framework import generics

from students.models.region import Region, District
from students.region.serializers.get.retrieve_view import RegionSerializer, DistrictSerializer
from students.region.serializers.crud.crud import create_regions


class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    create_regions()


class DistrictListView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        region_id = self.request.query_params.get('region_id')
        if region_id:
            return queryset.filter(region_id=region_id)
        return queryset.none()
