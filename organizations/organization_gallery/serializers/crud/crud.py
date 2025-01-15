from rest_framework import serializers
from organizations.models import OrganizationGallery
from organizations.models.models import File
from django.core.files.uploadedfile import InMemoryUploadedFile


class OrganizationGalleryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationGallery
        fields = '__all__'


class FileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

    def update(self, instance, validated_data):
        print(instance, validated_data)
        new_file = validated_data.pop('url', None)
        if new_file:
            instance.url.save(new_file.name, new_file)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

