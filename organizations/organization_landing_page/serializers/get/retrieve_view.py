from rest_framework import serializers
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding
from education.education.serializers.get.retriviev import EducationSerializer
from students.academic_year.serializers.get.retrieve_view import AcademicYearRetrieveSerializer
from organizations.organization_degree.serializers.get.retrieve_view import OrganizationDegreesRetrieveSerializer
from organizations.organization_fields.serializers.get.retrieve_view import OrganizationFieldsSerializer
from students.shift.serializers.get.retriviev import ShiftSerializer


class OrganizationLandingPageSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()
    education_language = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()
    field = serializers.SerializerMethodField()
    shift = serializers.SerializerMethodField()

    def get_education_language(self, obj):
        return EducationSerializer(obj.education_language).data

    def get_year(self, obj):
        return AcademicYearRetrieveSerializer(obj.year).data

    def get_degree(self, obj):
        return OrganizationDegreesRetrieveSerializer(obj.degree).data

    def get_organization(self, obj):
        return OrganizationSerializerForLanding(obj.organization).data

    def get_field(self, obj):
        return OrganizationFieldsSerializer(obj.field).data

    def get_shift(self, obj):
        return ShiftSerializer(obj.shift).data

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organization',
            'year',
            'desc',
            'expire_date',
            'degree',
            'grant',
            'education_language',
            'price',
            'requirements',
            'shift',
            'desc_json',
            'requirements_json',
            'field',
            'start_date'
        ]
