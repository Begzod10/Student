import datetime

from students.models.academic_year import AcademicYear
from rest_framework import serializers


class AcademicYearRetrieveSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    current_year = serializers.SerializerMethodField()
    current = serializers.SerializerMethodField()

    class Meta:
        model = AcademicYear
        fields = ['id', 'from_date', 'to', 'date', 'current_year', 'current']

    def get_from_date(self, obj):
        return obj.from_date.strftime('%Y')

    def get_to(self, obj):
        return obj.to.strftime('%Y')

    def get_date(self, obj):
        return f"{str(obj.from_date.strftime('%Y'))}-{str(obj.to.strftime('%Y'))}"

    def get_current_year(self, obj):
        return False if datetime.datetime.now().year != obj.from_date.year else True

    def get_current(self, obj):
        obj.current = True if datetime.datetime.now().year == obj.from_date.year else False
        obj.save()
        return obj.current
