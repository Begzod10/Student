from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from students.models.student import StudentRequest
from students.student_requests.serializers.crud.crud import StudentRequestCreateUpdateSerializer2


class StudentRequestCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentRequest.objects.all().select_related(
        'student__user', 'degree', 'shift', 'language', 'organization__organization_type', 'organization__region'
    )
    serializer_class = StudentRequestCreateUpdateSerializer2

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response({"msg": "Arizangiz topshirildi!"})
