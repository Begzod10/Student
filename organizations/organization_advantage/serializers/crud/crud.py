from rest_framework import serializers
from organizations.models.organization_landing_page import OrganizationAdvantage


class OrganizationAdvantageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationAdvantage
        fields = '__all__'
