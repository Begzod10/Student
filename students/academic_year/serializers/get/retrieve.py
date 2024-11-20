from students.models.academic_year import AcademicYear
from rest_framework import serializers


class AcademicYearRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = ['id', 'from_date', 'to']
