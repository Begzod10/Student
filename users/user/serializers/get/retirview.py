from rest_framework import serializers

from users.models import Users
from organizations.models import OrganizationUser


class RetrieveUserInfosForRegister(serializers.ModelSerializer):
    organization_id = serializers.SerializerMethodField()
    organization_name = serializers.SerializerMethodField()


    def get_organization_name(self, obj):
        return OrganizationUser.objects.filter(
            user=obj).first().organization.name if OrganizationUser.objects.filter(user=obj).exists() else None

    def get_organization_id(self, obj):
        return OrganizationUser.objects.filter(user=obj).first().organization.id if OrganizationUser.objects.filter(
            user=obj).exists() else None



    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'passport_seria', 'sex', 'born_date', 'born_address', 'indefikatsiya_pin',
                  'phone', "organization_id", "organization_name",
                  'phone_extra', 'email', 'role',"organization_user"]
