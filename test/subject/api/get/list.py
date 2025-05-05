from rest_framework import generics

from test.subject.serializers.get.get import SubjectSerializer
from test.models.subject import Subject


class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
