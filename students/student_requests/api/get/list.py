from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from students.models.student import StudentRequest
from students.student_requests.filters import StudentRequestFilter
from students.student_requests.serializers.get.get import StudentRequestListSerializer


class StudentRequestListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = StudentRequest.objects.all().select_related(
        'student__user', 'degree', 'shift', 'language', 'organization__organization_type', 'organization__region'
    )
    serializer_class = StudentRequestListSerializer
    filterset_class = StudentRequestFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        'student__user__name',
        'student__user__surname',
        'student__user__last_name'
    ]
