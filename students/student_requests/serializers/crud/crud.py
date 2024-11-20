from rest_framework import serializers

from students.models.student import StudentRequest, Student, Shift
from students.models.academic_year import AcademicYear
from organizations.models.models import Organization
from organizations.models.organization_fields import OrganizationFields
from education.models import EducationLanguage


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
