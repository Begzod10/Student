from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from students.models import Student, Region
from users.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(),
                                                write_only=True)  # Ensure region is processed correctly

    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):

        password = validated_data.pop('password')
        region = validated_data.pop('region', None)  # ✅ Remove region before creating Users
        role = validated_data.get('role', 'user')  # Default to 'user'

        user = Users.objects.create(**validated_data)  # ✅ No unexpected keyword arguments now
        user.set_password(password)
        user.save()

        if role == 'user' and region:  # ✅ Ensure region is not None
            Student.objects.create(user=user, region=region)  # ✅ Assign region to Student

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
                'student_id': user.student_set.first().id if user.student_set.exists() else None
            })
        except Users.DoesNotExist:
            data.update({"error": "User not found"})

        return data
