from rest_framework import serializers

from organizations.models.models import Organization
from organizations.models.organization_landing_page import OrganizationLandingPage, LandingPageShift, \
    OrganizationAdvantage


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'locations',
            'desc',
            'phone',
            'img',
            'organization_type',
            'region'
        ]


class OrganizationSerializerForLanding(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name'
        ]


class OrganizationHomeSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='organization.region.name', read_only=True)
    name = serializers.CharField(source='organization.name', read_only=True)
    locations = serializers.CharField(source='organization.locations', read_only=True)
    desc = serializers.SerializerMethodField()
    phone = serializers.CharField(source='organization.phone', read_only=True)
    img = serializers.CharField(source='organization.img', read_only=True)
    organization_type = serializers.CharField(source='organization.organization_type.name', read_only=True)
    landing_shift = serializers.SerializerMethodField()
    advantages = serializers.SerializerMethodField()
    degree = serializers.CharField(source='degree.name', read_only=True)

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'name',
            'locations',
            'desc',
            'phone',
            'img',
            'organization_type',
            'region',
            'start_date',
            'landing_shift',
            'advantages',
            'degree'
        ]

    def get_landing_shift(self, obj):
        obj = LandingPageShift.objects.filter(landing_page=obj).first()
        data = {
            'price': obj.price if obj else None,
        }

        return data

    def get_desc(self, obj):
        return f"{obj.organization.desc[:500]}..."

    def get_advantages(self, obj):
        text = OrganizationAdvantage.objects.filter(organization=obj.organization).first()
        return f"{text.desc[:500]}..."


class OrganizationDescSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='organization_type.name', read_only=True)
    class Meta:
        model = Organization
        fields = [
            'id',
            'desc',
            'type'
        ]
