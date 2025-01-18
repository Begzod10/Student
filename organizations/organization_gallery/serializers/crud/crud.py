from rest_framework import serializers
from organizations.models import OrganizationGallery
from organizations.models.models import File
from django.core.files.uploadedfile import InMemoryUploadedFile
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
    class Meta:
        model = OrganizationGallery
        fields = '__all__'

    def create(self, validated_data):
        file_data = validated_data.pop('file', None)
        print(f"File data received: {file_data}")

        if file_data:
            # Agar file_data File obyekti bo'lsa
            if isinstance(file_data, File):  # file_data File obyekti bo'lsa
                file_instance = file_data  # Faylni bevosita olish
            else:
                # Agar file_data boshqa formatda bo'lsa, ID yoki dict bo'lsa, uni olish kerak
                raise ValueError("Invalid file data format, expected a File object.")

            print(f"File instance: {file_instance}")  # Fayl obyektini tekshirish
            validated_data['file'] = file_instance

        return super().create(validated_data)
