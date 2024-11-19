from django.urls import path

from students.student_requests.api.crud.create import StudentRequestCreateView
from students.student_requests.api.crud.delete import StudentRequestDestroyView
from students.student_requests.api.get.profile import StudentRequestProfileView
from students.student_requests.api.get.list import StudentRequestListView
from students.student_requests.api.get.filter_items_for_organization_type import FilterItemsForOrganizationTypeView

urlpatterns = [
    path('create/', StudentRequestCreateView.as_view(), name='create'),
    path('update/<int:pk>', StudentRequestCreateView.as_view(), name='update'),
    path('delete/<int:pk>', StudentRequestDestroyView.as_view(), name='delete'),
    path('profile/<int:pk>', StudentRequestProfileView.as_view(), name='profile'),
    path('list/<int:pk>', StudentRequestListView.as_view(), name='list'),
    path('filter_items/', FilterItemsForOrganizationTypeView.as_view(), name='list'),
]
