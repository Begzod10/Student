from rest_framework import generics

from users.models import Users
from users.user.serializers.crud.serializers import RegisterSerializer, UserPasswordSerializer, UserPhotoSerializer


class UpdateUserInfo(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer


class UpdateUserPassword(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserPasswordSerializer


class UpdateUserPhoto(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserPhotoSerializer
