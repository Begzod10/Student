from rest_framework import serializers
from organizations.models.organization_landing_page import OrganizationAdvantage
from organizations.organization_gallery.serializers.get.retrieve_view import FileSerializer
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer


class OrganizationAdvantageCreateUpdateSerializer(serializers.ModelSerializer):
    file = FileSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = OrganizationAdvantage
        fields = ['id', 'name_optional', 'desc', 'file', 'organization']
