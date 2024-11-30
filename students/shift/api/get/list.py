from rest_framework import generics

from students.models.student import Shift
from students.shift.serializers.get.retriviev import ShiftSerializer


class ShiftList(generics.ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
