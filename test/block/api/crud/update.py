from rest_framework import generics, parsers
from test.models.test_block import TestBlock
from test.block.serializers.crud.crud import TestBlockSerializer


class UpdateBlockView(generics.UpdateAPIView):
    queryset = TestBlock.objects.all()
    serializer_class = TestBlockSerializer
    parser_classes = [parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser]
