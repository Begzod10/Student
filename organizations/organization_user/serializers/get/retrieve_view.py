from rest_framework import serializers
from organizations.models import OrganizationUser
from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'username', 'phone']


class OrganizationUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = OrganizationUser
        fields = ['id', 'user']
