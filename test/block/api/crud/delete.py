from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from test.models.test_block import TestBlock
from test.block.serializers.crud.crud import TestBlockSerializer


class TestBlockDeleteView(generics.DestroyAPIView):
    queryset = TestBlock.objects.all()
    serializer_class = TestBlockSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"detail": "TestBlock and related questions deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)
