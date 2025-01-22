from rest_framework import serializers

from education.models import EducationLanguage
from organizations.models.models import Organization
from organizations.models.organization_fields import OrganizationFields
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
        user = validated_data.pop('user')
        landing = validated_data.pop('landing')
        student = Student.objects.get(user=user)
        obj = StudentRequest.objects.create(
            student=student,
            organization=landing.organization,
            shift=landing.shift,
            field=landing.field,
            language=landing.education_language,
            year=landing.year,
            degree=landing.degree

        )

        return obj
