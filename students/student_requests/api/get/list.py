from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from students.models.student import StudentRequest, Student
from students.student_requests.filters import StudentRequestFilter
from students.student_requests.serializers.get.get import StudentRequestListSerializer


class StudentRequestListView(generics.ListAPIView):
    """
    API view to list student requests with filtering, search, and pagination.
    """
    # permission_classes = [permissions.IsAuthenticated]  # Ensure authentication

    queryset = StudentRequest.objects.select_related(
        'student__user', 'degree', 'shift', 'language',
        'organization__organization_type', 'organization__region'
    ).order_by('-id')  # Ensuring latest requests show first

    serializer_class = StudentRequestListSerializer
    filterset_class = StudentRequestFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        'student__user__name',
        'student__user__surname',
        'student__user__last_name'
    ]

    # def get_queryset(self):
    #     """
    #     Override get_queryset to apply additional filtering logic.
    #     """
    #     queryset = super().get_queryset()
    #     student_id = self.request.query_params.get('student_id')
    #
    #     if student_id:
    #         try:
    #             student = Student.objects.get(user_id=student_id)
    #             queryset = queryset.filter(student=student)
    #         except Student.DoesNotExist:
    #             return queryset.none()
    #     return queryset

    def list(self, request, *args, **kwargs):
        """
        Override list to manually serialize data for debugging.
        """
        if self.request.query_params.get('organization'):
            queryset = self.get_queryset().filter(organization_id=self.request.query_params.get('organization'))
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
