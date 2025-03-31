from django.urls import path

from test.test.api.crud.crud import TestCreateView, TestAddBlockView

urlpatterns = [
    path('create/', TestCreateView.as_view(), name='test-create'),
    path('add_block/<int:pk>/', TestAddBlockView.as_view(), name='test-update'),
]
