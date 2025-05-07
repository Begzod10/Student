from django.urls import path
from rest_framework.routers import DefaultRouter

from test.test.api.crud.add_block import TestAddBlockView
from test.test.api.crud.create import StudentTestViewSet
from test.test.api.crud.check import TestCheckView
from test.test.api.crud.create import TestCreateView, TestUpdateView
from test.test.api.crud.delete import TestDeleteView

router = DefaultRouter()
router.register(r'student-tests', StudentTestViewSet, basename='student-test')

urlpatterns = [
    path('create/', TestCreateView.as_view(), name='test-create'),
    path('update/<int:pk>/', TestUpdateView.as_view(), name='test-update'),
    path('add_block/<int:pk>/', TestAddBlockView.as_view(), name='test-update'),
    path('delete/<int:pk>/', TestDeleteView.as_view(), name='test-delete'),
    path('check/', TestCheckView.as_view(), name='test-check'),

]
urlpatterns += router.urls
