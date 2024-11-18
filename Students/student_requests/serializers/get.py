from rest_framework import serializers

from Students.models.student import StudentRequest, Student, Shift
from Students.models.academic_year import AcademicYear
from Organization.models.models import Organization
from Organization.models.organization_fields import OrganizationFields
from Education.models import EducationLanguage


class StudentRequestList(serializers.ModelSerializer):
    # direction
    name = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    class Meta:
        model = StudentRequest
        fields = ['id', 'name', 'phone', 'degree', 'shift', 'language', 'date']

    def get_name(self, obj):
        return f'{obj.student.user.name} {obj.student.user.surname} {obj.student.user.lastname}'

    def get_phone(self):
        return
