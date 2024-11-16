from django.urls import path
from Students.views import StudentRequestListView, StudentRequestRetrieveView, student_request_dashboard

urlpatterns = [
    path('student_request/<int:pk>/', StudentRequestRetrieveView.as_view(), name='student-request'),
    path('student_request_list/', StudentRequestListView.as_view(), name='student-request-list'),
    path('student-request-dashboard', student_request_dashboard, name='student_request_dashboard'),
]
