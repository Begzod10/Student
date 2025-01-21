from rest_framework import serializers
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding


class OrganizationLandingPageSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializerForLanding(source='organization_id')

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organization',
            'year_id',
            'desc',
            'expire_date',
            'degree_id',
            'grant',
            'education_language'
        ]
        depth = 1


