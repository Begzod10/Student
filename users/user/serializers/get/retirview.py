from rest_framework import serializers

from users.models import Users


class RetrieveUserInfosForRegister(serializers.ModelSerializer):
    organization_id = serializers.SerializerMethodField()
    organization_name = serializers.SerializerMethodField()
    organization_user = serializers.StringRelatedField(many=True, source='organization_users')

    def get_organization_name(self, obj):
        org_user = obj.organization_users.first()
        return org_user.organization.name if org_user else None

    def get_organization_id(self, obj):
        org_user = obj.organization_users.first()
        return org_user.organization.id if org_user else None
        return OrganizationUser.objects.filter(user=obj).first().organization.id if OrganizationUser.objects.filter(
            user=obj).exists() else None

    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'passport_seria', 'sex', 'born_date', 'born_address', 'indefikatsiya_pin',
                  'phone', "organization_id", "organization_name",
                  'passport_number', 'passport_pdf1', 'passport_pdf2',
                  'certificate', 'image',
                  'phone_extra', 'email', 'role', "organization_user"]
