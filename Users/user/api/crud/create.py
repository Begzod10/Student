from rest_framework import generics

from Users.models import Users
from Users.user.serializers import Register


class Register(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = Register
