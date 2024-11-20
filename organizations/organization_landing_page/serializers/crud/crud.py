from rest_framework import serializers

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding
from students.models import AcademicYear


class OrganizationLandingPageSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializerForLanding()

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organizations',
            'year_id',
            'desc',
            'name_optional',
            'expire_date',
            'degree_id'
        ]
        depth = 1

    def create(self, validated_data):
        year = validated_data.pop('year')
        get_year = AcademicYear.objects.get(year=year)
        return OrganizationLandingPage.objects.create(**validated_data, year_id=get_year)
