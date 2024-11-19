from rest_framework_simplejwt.views import TokenObtainPairView

from users.user.serializers.crud.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
