import pprint

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding, Organization
from students.models.academic_year import AcademicYear
from organizations.models.models import OrganizationDegrees
from organizations.organization_degree.serializers.get.retrieve_view import OrganizationDegreesRetrieveSerializer
from students.academic_year.serializers.get.retrieve_view import AcademicYearRetrieveSerializer
from education.education.serializers.get.retriviev import EducationSerializer, EducationLanguage


class OrganizationLandingPageCrudSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
    )
    education_language = serializers.PrimaryKeyRelatedField(
        queryset=EducationLanguage.objects.all()
    )
    degree = serializers.PrimaryKeyRelatedField(
        queryset=OrganizationDegrees.objects.all()
    )
    year = serializers.JSONField(write_only=True)
    message=serializers.SerializerMethodField()

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organization',
            'education_language',
            'year',
            'desc',
            'expire_date',
            'degree',
            'grant',
            'price',
            'requirements',
            'shift',
            'desc_json',
            'requirements_json',
            'field',
            'start_date',
            'message'
        ]

    def create(self, validated_data):
        year_id = validated_data.pop('year')
        academic_year = AcademicYear.objects.get(id=year_id)
        validated_data['year'] = academic_year
        validated_data['organization'] = validated_data.pop('organization')
        validated_data['degree'] = validated_data.pop('degree')
        validated_data['education_language'] = validated_data.pop('education_language')
        validated_data['desc'] = validated_data.pop('desc', '')
        validated_data['desc_json'] = validated_data.pop('desc_json', '')
        validated_data['shift'] = validated_data.pop('shift', None)
        validated_data['requirements'] = validated_data.pop('requirements', '')
        validated_data['price'] = validated_data.pop('price', None)
        validated_data['grant'] = validated_data.pop('grant', False)
        validated_data['expire_date'] = validated_data.pop('expire_date', None)
        validated_data['requirements_json'] = validated_data.pop('requirements_json', '')
        validated_data['start_date'] = validated_data.pop('start_date', None)
        self.custom_message = "E'lon muvaffaqiyatlik yaratildi!"
        return validated_data

    def get_message(self, obj):
        return getattr(self, 'custom_message', '')

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
        return {"msg": "Yo'nalish muvaffaqiyatli o'zgartirildi"}

    def delete(self, *args, **kwargs):
        """Override the delete method to mark the instance as deleted."""
        self.deleted = True
        self.save()
        return {"msg": "Yo'nalish muvaffaqiyatli o'chirildi"}
