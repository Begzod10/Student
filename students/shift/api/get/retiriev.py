from rest_framework import generics

from students.models import Shift
from students.shift.serializers.get.retriviev import ShiftSerializer


class ShiftRetrieve(generics.RetrieveAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftRetrievev2(generics.ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Shift.objects.none()
        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")

        return Shift.objects.filter(organization_type_id=pk)
