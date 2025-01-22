from django.urls import path

from students.shift.api.get.list import ShiftList
from students.shift.api.get.retiriev import ShiftRetrieve, ShiftRetrievev2

urlpatterns = [
    path('', ShiftList.as_view(), name='shift_list'),
    path('<int:pk>', ShiftRetrieve.as_view(), name='shift_retrieve'),
    path('list/<int:pk>/', ShiftRetrievev2.as_view(), name='shift_retrieve'),
]
