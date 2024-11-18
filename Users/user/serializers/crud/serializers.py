from rest_framework import serializers

from Users.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
