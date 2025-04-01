from rest_framework import generics
from test.models.models import Test
from test.test.serializers.crud.crud import TestUpdateSerializer


class TestAddBlockView(generics.UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestUpdateSerializer
