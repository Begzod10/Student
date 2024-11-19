from rest_framework import generics

from users.models import Users
from users.user.serializers.crud.serializers import RegisterSerializer


class Register(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
