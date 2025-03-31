from django.urls import path

from test.block.api.crud.update import UpdateBlockView

urlpatterns = [
    path('update/<int:pk>/', UpdateBlockView.as_view(), name='test-update'),
]
