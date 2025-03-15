from rest_framework import generics

from students.models.student import StudentRequest, Student
from students.student_requests.serializers.get.get import StudentRequestProfileSerializers


class StudentProfileRequest(generics.ListAPIView):
    queryset = StudentRequest.objects.all()
    serializer_class = StudentRequestProfileSerializers

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return StudentRequest.objects.none()
        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")
        user = Student.objects.get(user_id=pk)

        return StudentRequest.objects.filter(student=user).all()
