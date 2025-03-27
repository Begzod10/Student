from rest_framework import generics
from test.models.models import Test
from test.test.serializers.crud.crud import TestCreateSerializer, TestUpdateSerializer


class TestCreateView(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer


class TestUpdateView(generics.UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestUpdateSerializer
