from django.urls import path

from test.test.api.get.get import TestRetrieveView

urlpatterns = [
    path('test_retrieve/<int:pk>/', TestRetrieveView.as_view(), name='test-retrieve'),
]
