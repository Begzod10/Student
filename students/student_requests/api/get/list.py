from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from students.models.student import StudentRequest

from students.student_requests.serializers.get.get import StudentRequestListSerializer

from students.student_requests.filters import StudentRequestFilter


class StudentRequestListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentRequest.objects.all().select_related(
        'student__user', 'degree', 'shift', 'language', 'organization__organization_type', 'organization__region'
    )
    serializer_class = StudentRequestListSerializer
    filterset_class = StudentRequestFilter
    filter_backends = [DjangoFilterBackend]

