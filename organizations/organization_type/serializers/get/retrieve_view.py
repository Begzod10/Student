from rest_framework import serializers
from organizations.models.models import OrganizationType


class OrganizationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = '__all__'
        depth = 1

