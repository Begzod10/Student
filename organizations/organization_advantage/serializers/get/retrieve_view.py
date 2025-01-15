from organizations.models import File
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer
from rest_framework import serializers
from organizations.models.organization_landing_page import OrganizationAdvantage


class File2Serializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class OrganizationAdvantageSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    file = File2Serializer()

    class Meta:
        model = OrganizationAdvantage
        fields = '__all__'
