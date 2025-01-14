from rest_framework import serializers

from organizations.models.models import OrganizationType


class OrganizationTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = '__all__'
