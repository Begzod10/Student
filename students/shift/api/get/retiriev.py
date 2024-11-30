from rest_framework import generics
from students.models import Shift
from students.shift.serializers.get.retriviev import ShiftSerializer


class ShiftRetrieve(generics.RetrieveAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer