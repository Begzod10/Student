from rest_framework import serializers

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding
from students.models.academic_year import AcademicYear
from organizations.models.models import OrganizationDegrees
from organizations.organization_degree.serializers.get.retrieve_view import OrganizationDegreesRetrieveSerializer
from students.academic_year.serializers.get.retrieve_view import AcademicYearRetrieveSerializer


class OrganizationLandingPageSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializerForLanding()
    year = AcademicYearRetrieveSerializer()
    degree = OrganizationDegreesRetrieveSerializer()

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organization',
            'year',
            'desc',
            'name_optional',
            'expire_date',
            'degree'
        ]
        depth = 1

    def create(self, validated_data):
        year = validated_data.pop('year')
        degree = validated_data.pop('degree')
        get_year = AcademicYear.objects.get(year=year)
        get_degree = OrganizationDegrees.objects.get(degree=degree)
        return OrganizationLandingPage.objects.create(**validated_data, year_id=get_year, degree_id=get_degree)

    def update(self, instance, validated_data):
        year = validated_data.pop('year')
        degree = validated_data.pop('degree')
        get_year = AcademicYear.objects.get(year=year)
        get_degree = OrganizationDegrees.objects.get(degree=degree)
        instance.year_id = get_year
        instance.degree_id = get_degree
        instance.save()
        return instance  # Return the updated instance
