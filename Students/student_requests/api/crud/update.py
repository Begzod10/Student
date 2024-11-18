from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Students.models.student import StudentRequest

from Students.student_requests.serializers.crud import StudentRequestCreateUpdateSerializer


class StudentRequestUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentRequest.objects.all()
    serializer_class = StudentRequestCreateUpdateSerializer
