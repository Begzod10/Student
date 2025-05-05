from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models.student import StudentRequest

from students.student_requests.serializers.crud.crud import StudentRequestCreateUpdateSerializer


class StudentRequestUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = StudentRequest.objects.all().select_related(
        'student__user', 'degree', 'shift', 'language', 'organization__organization_type', 'organization__region'
    )
    serializer_class = StudentRequestCreateUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        status = request.data.get('status')
        instance.request_status = status
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # self.perform_update(serializers)
        return Response(serializer.data)
