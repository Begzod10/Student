from rest_framework import serializers

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding, Organization
from students.models.academic_year import AcademicYear
from organizations.models.models import OrganizationDegrees
from organizations.organization_degree.serializers.get.retrieve_view import OrganizationDegreesRetrieveSerializer
from students.academic_year.serializers.get.retrieve_view import AcademicYearRetrieveSerializer
from education.education.serializers.get.retriviev import EducationSerializer, EducationLanguage


class OrganizationLandingPageCrudSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(), source="organization_id"
    )
    education_language = serializers.PrimaryKeyRelatedField(
        queryset=EducationLanguage.objects.all()
    )
    degree = serializers.PrimaryKeyRelatedField(
        queryset=OrganizationDegrees.objects.all(), source="degree_id"
    )
    year = serializers.JSONField(write_only=True)

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organization',
            'education_language',
            'year',
            'desc',
            'name_optional',
            'expire_date',
            'degree',
            'grant',
            'deleted',
        ]

    def create(self, validated_data):
        year_data = validated_data.pop('year')
        from_date = year_data.get('from_date')
        to_date = year_data.get('to')
        academic_year, _ = AcademicYear.objects.get_or_create(
            from_date=from_date, to=to_date
        )
        validated_data['year_id'] = academic_year
        validated_data['organization_id'] = validated_data.pop('organization_id')
        validated_data['degree_id'] = validated_data.pop('degree_id')
        return OrganizationLandingPage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        year_data = validated_data.pop('year', None)
        if year_data:
            from_date = year_data.get('from_date')
            to_date = year_data.get('to')
            academic_year, _ = AcademicYear.objects.get_or_create(
                from_date=from_date, to=to_date
            )
            instance.year_id = academic_year
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
