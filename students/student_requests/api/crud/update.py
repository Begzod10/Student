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
        if status == "rejectedRequest":
            instance.cancel = True
            instance.request_status = "rejectedRequest"
        elif status == "acceptedRequest":
            instance.accept = True
            instance.request_status = "acceptedRequest"
        elif status == "returnRequest":
            instance.back_recovery = True
            instance.request_status = "returnRequest"
        elif status == "invitedRequest":
            instance.called_to_exam = True
            instance.request_status = "invitedRequest"
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)
        return Response(serializer.data)
