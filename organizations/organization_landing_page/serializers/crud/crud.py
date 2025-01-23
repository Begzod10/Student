import pprint

from rest_framework import serializers

from education.education.serializers.get.retriviev import EducationLanguage
from organizations.models.models import OrganizationDegrees
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import Organization
from students.models.academic_year import AcademicYear


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

    message = serializers.SerializerMethodField()

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

    def validate_year(self, value):
        academic_year = AcademicYear.objects.get(id=value)
        return academic_year

    def get_message(self, obj):
        return "E'lon muvaffaqiyatlik yaratildi!"
    def update(self, instance, validated_data):
        pprint.pprint(validated_data)

        instance.year = validated_data.pop('year', None)
        instance.organization = validated_data.pop('organization', None)
        instance.degree = validated_data.pop('degree')
        instance.education_language = validated_data.pop('education_language')
        instance.desc = validated_data.pop('desc', '')
        instance.desc_json = validated_data.pop('desc_json', '')
        instance.shift = validated_data.pop('shift', None)
        instance.requirements = validated_data.pop('requirements', '')
        instance.price = validated_data.pop('price', None)
        instance.grant = validated_data.pop('grant', False)
        instance.expire_date = validated_data.pop('expire_date', None)
        instance.requirements_json = validated_data.pop('requirements_json', '')
        instance.start_date = validated_data.pop('start_date', None)

        instance.save()

        return {"msg": "Yo'nalish muvaffaqiyatli o'zgartirildi"}

    def delete(self, *args, **kwargs):
        """Override the delete method to mark the instance as deleted."""
        self.deleted = True
        self.save()
        return {"msg": "Yo'nalish muvaffaqiyatli o'chirildi"}


class OrganizationLandingPageUpdateSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
    )
    education_language = serializers.PrimaryKeyRelatedField(
        queryset=EducationLanguage.objects.all()
    )
    degree = serializers.PrimaryKeyRelatedField(
        queryset=OrganizationDegrees.objects.all()
    )
    year = serializers.PrimaryKeyRelatedField(
        queryset=AcademicYear.objects.all()
    )

    message = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationLandingPage
        fields = ['id', 'organization', 'education_language', 'year', 'desc', 'expire_date', 'degree', 'grant',
                  'price', 'requirements', 'shift', 'desc_json', 'requirements_json', 'field', 'start_date', 'message']

    def get_message(self, obj):
        return getattr(self, 'custom_message', "Yo'nalish muvaffaqiyatli o'zgartirildi")

    def update(self, instance, validated_data):
        print(validated_data)
        return super().update(instance, validated_data)
