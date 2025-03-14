from rest_framework import serializers
from organizations.models import OrganizationUser
from users.models import Users
from organizations.organization_gallery.serializers.get.retrieve_view import FileSerializer


class UserSerializer(serializers.ModelSerializer):
    file = FileSerializer()

    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'username', 'phone_extra', 'file']


class OrganizationUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = OrganizationUser
        fields = ['id', 'user']
