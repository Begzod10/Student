import pprint

from rest_framework import generics

from students.models.notification import Notification
from students.models.student import Student
from students.notification.serializers import NotificationSerializer, NotificationOrganizationSerializer
from organizations.models.models import Organization


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
        organization_id = self.request.query_params.get('organization_id', None)
        student_id = self.request.query_params.get('student_id', None)
        organization = Organization.objects.get(id=organization_id)

        try:
            student = Student.objects.get(user_id=student_id)
        except Student.DoesNotExist:
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return Notification.objects.none()
        if type_param == 'student':

            notifications = Notification.objects.filter(student=student, organization=organization).select_related(
                'organization').order_by('id')

            return notifications

        elif type_param == 'organization':
            organization_id = self.kwargs['pk']

            return Notification.objects.filter(organization_id=organization_id, student=student).select_related(
                'student').order_by('id')

        return Notification.objects.none()


# class NotificationForOrganizationView(generics.ListAPIView):
#     serializer_class = NotificationOrganizationSerializer
#
#     def get_queryset(self):
#
#         try:
#             student = Student.objects.get(user_id=self.kwargs['pk'])
#         except Student.DoesNotExist:
#             try:
#                 student = Student.objects.get(id=self.kwargs['pk'])
#             except Student.DoesNotExist:
#                 return Notification.objects.none()
#         notifications = Notification.objects.filter(student=student).select_related('organization').order_by('id')
#         return Organization.objects.filter(id__in=[notification.organization_id for notification in notifications]).distinct()

class NotificationForOrganizationView(generics.ListAPIView):
    serializer_class = NotificationOrganizationSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Organization.objects.none()

        try:
            student = Student.objects.get(user_id=self.kwargs['pk'])
        except Student.DoesNotExist:
            try:
                student = Student.objects.get(id=self.kwargs['pk'])
            except Student.DoesNotExist:
                return Notification.objects.none()

        notifications = Notification.objects.filter(student=student).select_related('organization').order_by('id')
        return Organization.objects.filter(
            id__in=[notification.organization_id for notification in notifications]).distinct()
