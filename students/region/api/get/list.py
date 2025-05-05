from rest_framework import generics

from students.models.region import Region, District
from students.region.serializers.crud.crud import create_regions
from students.region.serializers.get.retrieve_view import RegionSerializer, DistrictSerializer


class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    create_regions()


class DistrictListView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        region_ids = self.request.query_params.get('region_id')
        if region_ids:
            region_id_list = [int(id.strip()) for id in region_ids.split(',') if id.strip().isdigit()]
            return queryset.filter(region_id__in=region_id_list)
        return queryset.none()
