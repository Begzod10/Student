from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from students.models.student import StudentRequest

from students.student_requests.serializers.get.get import StudentRequestProfileSerializer


class StudentRequestProfileView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = StudentRequest.objects.all().select_related(
        'student__user', 'degree', 'shift', 'language', 'organization__organization_type', 'organization__region'
    )
    serializer_class = StudentRequestProfileSerializer
