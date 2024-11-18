from rest_framework import serializers
from Organization.models import OrganizationLandingPage
from .organization_sr import OrganizationSerializerForLanding


class OrganizationLandingPageSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializerForLanding()

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organization',
            'year_id',
            'desc',
            'name_optional',
            'expire_date',
            'degree_id'
        ]
        depth = 1  # This will automatically include the related data for ForeignKey fields.
