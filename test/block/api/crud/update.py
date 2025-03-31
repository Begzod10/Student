from rest_framework import generics
from test.models.subject import Subject
from test.block.serializers.crud.crud import TestBlockSerializer


class UpdateBlockView(generics.UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = TestBlockSerializer
