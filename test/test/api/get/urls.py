from django.urls import path

from test.test.api.get.get import TestRetrieveView, TestListApiView, TestListApiViewForHome, \
    StudentTestResultListApiView, StudentTestResultDeleteApiView, TestRetrieveViewForHome

urlpatterns = [
    path('test_retrieve/<int:pk>/', TestRetrieveView.as_view(), name='test-retrieve'),
    path('test_list/', TestListApiView.as_view(), name='test-list'),
    path('test_list_home/', TestListApiViewForHome.as_view(), name='test-list-home'),
    path('test_result_list/', StudentTestResultListApiView.as_view(), name='test-list'),
    path('test_result_delete/<int:pk>/', StudentTestResultDeleteApiView.as_view(), name='test-list'),
    path('get_test/', TestRetrieveViewForHome.as_view(), name='get-test'),
]
