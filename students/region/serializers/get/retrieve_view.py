from students.models.region import Region
from rest_framework import serializers


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']
        depth = 1

    def create(self, validated_data):
        region, created = Region.objects.get_or_create(**validated_data)
        return region
