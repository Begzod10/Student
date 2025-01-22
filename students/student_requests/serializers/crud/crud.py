from django.shortcuts import get_object_or_404
from rest_framework import serializers

from education.models import EducationLanguage
from organizations.models.models import Organization
from organizations.models.organization_fields import OrganizationFields
from organizations.models.organization_landing_page import OrganizationLandingPage
from students.models.academic_year import AcademicYear
from students.models.student import StudentRequest, Student, Shift


class StudentRequestCreateUpdateSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    shift = serializers.PrimaryKeyRelatedField(queryset=Shift.objects.all())
    field = serializers.PrimaryKeyRelatedField(queryset=OrganizationFields.objects.all())
    language = serializers.PrimaryKeyRelatedField(queryset=EducationLanguage.objects.all())
    year = serializers.PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())

    class Meta:
        model = StudentRequest
        fields = ['id', 'student', 'organization', 'shift', 'field', 'language', 'year', 'accepted', 'canceled',
                  'back_recovery', 'back_recovery', 'present_in_exam', 'evaluated', 'contract_given', 'payed_status',
                  'accepted_to_study', 'degree']


class StudentRequestCreateUpdateSerializer2(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    landing = serializers.CharField(required=False)

    class Meta:
        model = StudentRequest
        fields = ['user', 'landing']

    def create(self, validated_data):
        user_id = validated_data.get('user')
        landing_id = validated_data.get('landing')

        landing_page = get_object_or_404(OrganizationLandingPage, id=landing_id)
        student = get_object_or_404(Student, user=user_id)

        if StudentRequest.objects.filter(
                student=student,
                organization=landing_page.organization,
                shift=landing_page.shift,
                field=landing_page.field,
                language=landing_page.education_language,
                year=landing_page.year,
                degree=landing_page.degree,
                landing_page=landing_page,
        ).exists():
            raise serializers.ValidationError({"detail": "Siz allaqachon bu yo'nalishdan ro'yhatdan o'tgansiz!"})

        obj = StudentRequest.objects.create(
            student=student,
            organization=landing_page.organization,
            shift=landing_page.shift,
            field=landing_page.field,
            language=landing_page.education_language,
            year=landing_page.year,
            degree=landing_page.degree,
            landing_page=landing_page,
        )

        return {"detail": "Arizangiz topshirildi!"}
