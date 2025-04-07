import pprint

from rest_framework import serializers

from education.education.serializers.get.retriviev import EducationLanguage
from organizations.models.models import OrganizationDegrees
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import Organization
from students.models.academic_year import AcademicYear
from organizations.models.organization_fields import OrganizationFields
from students.models.student import Shift


class OrganizationLandingPageCrudSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=OrganizationFields.objects.all(),
    )
    degree = serializers.PrimaryKeyRelatedField(
        queryset=OrganizationDegrees.objects.all()
    )
    year = serializers.IntegerField(write_only=True)  # expects just an ID

    message = serializers.SerializerMethodField()

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
            'price',
            'requirements',
            'desc_json',
            'requirements_json',
            'field',
            'start_date',
            'message',
            # 'education_language',  <-- not included
            # 'shift',               <-- not included
        ]

    def validate_year(self, value):
        try:
            return AcademicYear.objects.get(id=value)
        except AcademicYear.DoesNotExist:
            raise serializers.ValidationError("Academic year not found.")

    def get_message(self, obj):
        return "E'lon muvaffaqiyatlik yaratildi!"

    def create(self, validated_data):

        request = self.context.get('request')

        education_language_id = request.data.get('education_language', [])
        shift_id = request.data.get('shift', [])
        education_language_ids = [item['value'] for item in education_language_id]
        shift_ids = [item['value'] for item in shift_id]

        education_language_qs = EducationLanguage.objects.filter(id__in=education_language_ids)
        shift_qs = Shift.objects.filter(id__in=shift_ids)

        landing_page = OrganizationLandingPage.objects.create(**validated_data)

        landing_page.education_language.set(education_language_qs)
        landing_page.shift.set(shift_qs)

        return landing_page

    def update(self, instance, validated_data):
        instance.year = validated_data.pop('year', None)
        instance.organization = validated_data.pop('organization', instance.organization)
        instance.degree = validated_data.pop('degree', instance.degree)
        instance.desc = validated_data.pop('desc', instance.desc)
        instance.desc_json = validated_data.pop('desc_json', instance.desc_json)
        instance.requirements = validated_data.pop('requirements', instance.requirements)
        instance.price = validated_data.pop('price', instance.price)
        instance.grant = validated_data.pop('grant', instance.grant)
        instance.expire_date = validated_data.pop('expire_date', instance.expire_date)
        instance.requirements_json = validated_data.pop('requirements_json', instance.requirements_json)
        instance.start_date = validated_data.pop('start_date', instance.start_date)
        instance.field = validated_data.pop('field', instance.field)

        instance.save()

        request = self.context.get('request')

        education_language_id = request.data.get('education_language', [])
        shift_id = request.data.get('shift', [])
        education_language_ids = [item['value'] for item in education_language_id]
        shift_ids = [item['value'] for item in shift_id]

        education_language_qs = EducationLanguage.objects.filter(id__in=education_language_ids)
        shift_qs = Shift.objects.filter(id__in=shift_ids)

        for lang in instance.education_language.all():
            instance.education_language.remove(lang)

        for shift in instance.shift.all():
            instance.shift.remove(shift)
        instance.save()

        instance.education_language.set(education_language_qs)
        instance.shift.set(shift_qs)
        instance.save()
        return instance

    # def delete(self, *args, **kwargs):
    #     """Override the delete method to mark the instance as deleted."""
    #     self.deleted = True
    #     self.save()
    #     return Response({"message": "Yo'nalish muvaffaqiyatli o'chirildi"}, status=200)


class OrganizationLandingPageUpdateSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
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
        fields = ['id', 'organization',  'year', 'desc', 'expire_date', 'degree', 'grant',
                  'price', 'requirements', 'desc_json', 'requirements_json', 'field', 'start_date', 'message']

    def get_message(self, obj):
        return getattr(self, 'custom_message', "Yo'nalish muvaffaqiyatli o'zgartirildi")

    def update(self, instance, validated_data):
        instance.year = validated_data.pop('year', None)
        instance.organization = validated_data.pop('organization', instance.organization)
        instance.degree = validated_data.pop('degree', instance.degree)
        instance.desc = validated_data.pop('desc', instance.desc)
        instance.desc_json = validated_data.pop('desc_json', instance.desc_json)
        instance.requirements = validated_data.pop('requirements', instance.requirements)
        instance.price = validated_data.pop('price', instance.price)
        instance.grant = validated_data.pop('grant', instance.grant)
        instance.expire_date = validated_data.pop('expire_date', instance.expire_date)
        instance.requirements_json = validated_data.pop('requirements_json', instance.requirements_json)
        instance.start_date = validated_data.pop('start_date', instance.start_date)
        instance.field = validated_data.pop('field', instance.field)
        instance.save()
        request = self.context.get('request')
        education_language_id = request.data.get('education_language', [])
        shift_id = request.data.get('shift', [])
        education_language_ids = [item['value'] for item in education_language_id]
        shift_ids = [item['value'] for item in shift_id]

        education_language_qs = EducationLanguage.objects.filter(id__in=education_language_ids)
        shift_qs = Shift.objects.filter(id__in=shift_ids)

        for lang in instance.education_language.all():
            instance.education_language.remove(lang)

        for shift in instance.shift.all():
            instance.shift.remove(shift)
        instance.save()

        instance.education_language.set(education_language_qs)
        instance.shift.set(shift_qs)
        instance.save()
        return instance
