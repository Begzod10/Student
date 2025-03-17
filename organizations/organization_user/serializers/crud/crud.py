from rest_framework import serializers
from organizations.models import OrganizationUser, Jobs, OrganizationType, Organization
from users.models import Users
from django.core.exceptions import ValidationError

from rest_framework.response import Response


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer to handle creating a new user with default values.
    """

    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'username', 'phone_extra', 'file']

    def create(self, validated_data):
        print(validated_data)
        exists = Users.objects.filter(phone=validated_data['phone_extra']).exists()
        exists_user = Users.objects.filter(username=validated_data['username']).exists()
        if exists:
            return Response({"phone": "Users with this phone already exists."})
        if exists_user:
            return Response({"username": "Users with this username already exists."})
        user = Users.objects.create(**validated_data)
        user.set_password("12345678")
        user.role = "organization"
        user.save()
        return user


class OrganizationUserCreateUpdateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = OrganizationUser
        fields = ['id', 'user', 'organization']

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            file_id = user_data['file'].id if 'file' in user_data else None
            user_data['file'] = file_id
            user_serializer = UserCreateSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            validated_data['user'] = user
        job = Jobs.objects.get(name='organization')
        validated_data['job'] = job
        return OrganizationUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            if user_data.get('phone'):
                if user_data.get('phone') != instance.user.phone:
                    if Users.objects.filter(phone=user_data.get('phone')).exclude(id=instance.user.id).exists():
                        raise ValidationError({"phone": "Users with this phone already exists."})

            if user_data.get('username'):
                if user_data.get('username') != instance.user.username:
                    if Users.objects.filter(username=user_data.get('username')).exclude(id=instance.user.id).exists():
                        raise ValidationError({"username": "Users with this username already exists."})
            file_id = user_data['file'].id if 'file' in user_data else None
            user_data['file'] = file_id

            user_serializer = UserCreateSerializer(instance=instance.user, data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            print(instance.user)
            validated_data['user'] = instance.user

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        user = instance.user
        get_user = Users.objects.get(id=user.id)
        print(get_user)
        get_user.delete()
        instance.delete()
        user.delete()
        return {

            "message": "OrganizationUser and associated user deleted successfully."
        }
