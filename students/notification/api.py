import pprint

from rest_framework import generics

from students.models.notification import Notification
from students.models.student import Student
from students.notification.serializers import NotificationSerializer
from organizations.models.models import Organization
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer


class NotificationRetrieve(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationCreateView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationUpdateView(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDestroyView(generics.DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationForStudentView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param == 'student':
            try:
                student = Student.objects.get(user_id=self.kwargs['pk'])
            except Student.DoesNotExist:
                try:
                    student = Student.objects.get(id=self.kwargs['pk'])
                except Student.DoesNotExist:
                    return Notification.objects.none()
            notifications = Notification.objects.filter(student=student).select_related('organization').order_by('id')

            return notifications

        elif type_param == 'organization':
            organization_id = self.kwargs['pk']
            return Notification.objects.filter(organization_id=organization_id).select_related('student').order_by('id')

        return Notification.objects.none()
