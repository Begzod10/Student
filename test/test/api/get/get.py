from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from test.models.models import Test
from test.test.filtersets.testflter import TestFilter
from test.test.serializers.get.get import TestRetrieveSerializer, TestListSerializer


class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestRetrieveSerializer


class TestListApiView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TestFilter


class TestListApiViewForHome(APIView):
    def get(self, request):
        tests = Test.objects.exclude(is_mandatory=True).all()
        serializer = TestListSerializer(tests, many=True)
        return Response(serializer.data)
