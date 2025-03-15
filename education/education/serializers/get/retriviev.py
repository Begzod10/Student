from rest_framework import serializers

from education.models import EducationLanguage


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLanguage
        fields = '__all__'
