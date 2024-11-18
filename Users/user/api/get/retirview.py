from rest_framework import generics

from Users.models import Users
from Users.user.serializers.get.retirview import RetrieveUserInfosForRegister


class RetrieveUserInfos(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = RetrieveUserInfosForRegister
