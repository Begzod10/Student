from rest_framework import generics

from users.models import Users
from users.user.serializers.get.retirview import RetrieveUserInfosForRegister


class RetrieveUserInfos(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = RetrieveUserInfosForRegister
