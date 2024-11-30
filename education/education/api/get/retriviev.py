from rest_framework import generics
from education.models import EducationLanguage
from education.education.serializers.get.retriviev import EducationSerializer


class EducationRetrieve(generics.RetrieveAPIView):
    queryset = EducationLanguage.objects.all()
    serializer_class = EducationSerializer