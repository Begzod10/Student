from rest_framework import generics

from users.models import Users
from users.user.serializers import Register


class Register(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = Register
