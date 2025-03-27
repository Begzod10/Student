from django.urls import path

from test.test.api.crud.crud import TestCreateView, TestUpdateView

urlpatterns = [
    path('create/', TestCreateView.as_view(), name='test-create'),
]
