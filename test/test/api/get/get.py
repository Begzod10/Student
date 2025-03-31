from rest_framework import generics
from test.models.models import Test
from test.test.serializers.get.get import TestRetrieveSerializer, TestListSerializer
from rest_framework import generics


class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestRetrieveSerializer


class TestListApiView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer
