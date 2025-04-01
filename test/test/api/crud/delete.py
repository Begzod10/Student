from rest_framework import generics
from test.models.models import Test
from test.test.serializers.crud.crud import TestCreateSerializer


class TestDeleteView(generics.DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer
