from django.urls import path
from students.student_requests.views import StudentRequestListView, StudentRequestRetrieveView, \
    student_request_dashboard
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('student_request_list/', StudentRequestListView.as_view(), name='student-request-list'),
    path('student-request-dashboard', student_request_dashboard, name='student_request_dashboard'),
    path('student_requests/', include('students.student_requests.urls')),
    path('region/crud/', include('students.region.api.crud.urls')),
    path('student_request/<int:pk>/', StudentRequestRetrieveView.as_view(), name='student-request'),
    path('acedemic_year/', include('students.academic_year.api.get.urls')),
    path('shift/', include('students.shift.api.get.urls')),
]
