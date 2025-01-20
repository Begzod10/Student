from rest_framework import serializers
from organizations.models import OrganizationGallery
from organizations.models.models import File
from organizations.organization_gallery.serializers.get.retrieve_view import FileSerializer


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


class OrganizationGalleryCreateUpdateSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)
    file_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = OrganizationGallery
        fields = ['id', 'file', 'file_id', 'organization']

    def create(self, validated_data):
        file_id = validated_data.pop('file_id', None)
        try:
            file_instance = File.objects.get(id=file_id)
            validated_data['file'] = file_instance
        except File.DoesNotExist:
            raise serializers.ValidationError({"file_id": "File with the given ID does not exist."})
        return super().create(validated_data)