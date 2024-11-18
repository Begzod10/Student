from rest_framework import generics

from Users.models import Users
from Users.user.serializers.crud.serializers import RegisterSerializer


class UpdateUserInfo(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
