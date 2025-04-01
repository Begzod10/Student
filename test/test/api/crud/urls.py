from django.urls import path

from test.test.api.crud.create import TestCreateView
from test.test.api.crud.add_block import TestAddBlockView
from test.test.api.crud.delete import TestDeleteView

urlpatterns = [
    path('create/', TestCreateView.as_view(), name='test-create'),
    path('add_block/<int:pk>/', TestAddBlockView.as_view(), name='test-update'),
    path('delete/<int:pk>/', TestDeleteView.as_view(), name='test-delete'),
]
