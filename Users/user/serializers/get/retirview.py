from rest_framework import serializers

from Users.models import Users


class RetrieveUserInfosForRegister(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'passport_seria', 'sex', 'born_date', 'born_address', 'indefikatsiya_pin',
                  'phone',
                  'phone_extra', 'email']

