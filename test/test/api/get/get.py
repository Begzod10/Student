from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from test.models.models import Test
from test.test.serializers.get.get import TestRetrieveSerializer, TestListSerializer
from test.test.filtersets.testflter import TestFilter


class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestRetrieveSerializer


class TestListApiView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TestFilter
