from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from students.models import Student
from users.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        role = validated_data.get('role')
        if role is None:
            role = 'user'
        user = Users.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        if role == 'user':
            Student.objects.create(user=user)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['phone'] = user.phone

        return token

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        user = authenticate(phone=phone, password=password)
        if not user:
            print(phone, password)
            user = authenticate(username=phone, password=password)
            if not user:
                raise AuthenticationFailed({'detail': "Telefon raqam yoki parol noto‘g‘ri", 'status': False})

        if not user.is_active:
            raise AuthenticationFailed('Foydalanuvchi faol emas')

        return super().validate(attrs)


from rest_framework_simplejwt.tokens import AccessToken


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        access_token = data.get("access")
        refresh_token = attrs.get("refresh")
        decoded_token = AccessToken(access_token)

        user_id = decoded_token.get("user_id")

        try:
            user = Users.objects.get(id=user_id)
            data.update({
                "refresh": refresh_token,
                "access": access_token,
                "id": user.id,
                "name": user.name,
                "surname": user.surname,
                "sex": user.sex,
                "born_date": user.born_date,
                "email": user.email,
            })
        except Users.DoesNotExist:
            data.update({"error": "User not found"})

        return data
