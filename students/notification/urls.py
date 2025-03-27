from django.urls import path
from .api import NotificationCreateView, NotificationUpdateView, NotificationDestroyView, NotificationForStudentView, \
    NotificationForOrganizationView

urlpatterns = [
    path('create/', NotificationCreateView.as_view(), name='notification-create'),
    path('update/<int:pk>', NotificationCreateView.as_view(), name='notification-update'),
    path('destroy/<int:pk>', NotificationCreateView.as_view(), name='notification-delete'),
    path('get_organization/', NotificationForStudentView.as_view(), name='notification'),
    path('get_organization_student/<int:pk>', NotificationForOrganizationView.as_view(),
         name='notification-for-student'),
]
