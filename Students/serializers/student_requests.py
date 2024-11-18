from rest_framework import serializers

from ..models.student import StudentRequest, Student, Shift
from Organization.models.models import Organization


class StudentRequestCreateUpdateSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    shift = serializers.PrimaryKeyRelatedField(queryset=Shift.objects.all())

    class Meta:
        model = StudentRequest
        fields = ['id', 'class_number', 'subject', 'hours']
