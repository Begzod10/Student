from django.urls import path

from Students.student_requests.api.crud.create import StudentRequestCreateView
from Students.student_requests.api.crud.delete import StudentRequestDestroyView

urlpatterns = [
    path('create/', StudentRequestCreateView.as_view(), name='requests_create'),
    path('update/<int:pk>', StudentRequestCreateView.as_view(), name='requests_create'),
    path('delete/<int:pk>', StudentRequestDestroyView.as_view(), name='requests_create'),
    # path('delete/<int:pk>', StudentRequestDestroyView.as_view(), name='requests_create'),

]
