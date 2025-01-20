from rest_framework import serializers
from organizations.models import OrganizationGallery, File, Organization
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class OrganizationGallerySerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    file = FileSerializer()

    class Meta:
        model = OrganizationGallery
        fields = ['id', 'file', 'organization']
