from django.urls import path

from test.test.api.get.get import TestRetrieveView, TestListApiView

urlpatterns = [
    path('test_retrieve/<int:pk>/', TestRetrieveView.as_view(), name='test-retrieve'),
    path('test_list/', TestListApiView.as_view(), name='test-list'),
]
