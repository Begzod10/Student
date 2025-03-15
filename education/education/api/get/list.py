from rest_framework import generics

from education.education.serializers.get.retriviev import EducationSerializer
from education.models import EducationLanguage


class EducationList(generics.ListAPIView):
    queryset = EducationLanguage.objects.all()
    serializer_class = EducationSerializer
