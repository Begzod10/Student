from django.urls import path

from test.block.api.crud.update import UpdateBlockView
from test.block.api.crud.delete import TestBlockDeleteView

urlpatterns = [
    path('update/<int:pk>/', UpdateBlockView.as_view(), name='test-update'),
    path('delete/<int:pk>/', TestBlockDeleteView.as_view(), name='test-delete'),
]
