from rest_framework import generics
from test.models.models import Test
from test.test.serializers.crud.crud import TestCreateSerializer
from rest_framework.response import Response
from rest_framework import status


class TestDeleteView(generics.DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Test deleted successfully."}, status=status.HTTP_200_OK)
