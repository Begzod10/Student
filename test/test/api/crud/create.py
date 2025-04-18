from rest_framework import generics, status
from rest_framework.response import Response
from test.models.models import Test
from test.test.serializers.crud.crud import TestCreateSerializer
from test.test.serializers.get.get import TestRetrieveSerializer
from test.models.subject import Subject


class TestCreateView(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = self.get_queryset().get(id=response.data['id'])
        return Response(TestRetrieveSerializer(instance).data, status=status.HTTP_201_CREATED)
