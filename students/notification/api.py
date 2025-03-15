from rest_framework import generics

from students.models.notification import Notification
from students.notification.serializers import NotificationSerializer
from organizations.models import Organization
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
        student = self.request.user.student  # Assuming User has a related Student object

        # Get all notifications for the student
        get_notification = Notification.objects.filter(student=student)

        # Extract unique organization IDs from these notifications
        organization_ids = get_notification.values_list("organization_id", flat=True).distinct()

        # Filter organizations based on the extracted organization IDs
        organizations = Organization.objects.filter(id__in=organization_ids)

        return OrganizationSerializer(organizations, many=True).data
