from django.urls import path

from test.subject.api.get.list import SubjectListCreateView

urlpatterns = [
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list'),
]
