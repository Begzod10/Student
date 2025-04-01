from django.urls import path

from test.question.api.crud.update import TestQuestionUpdateDeleteView

urlpatterns = [
    path('update_delete/<int:pk>/', TestQuestionUpdateDeleteView.as_view(), name='test-update-delete'),
]
