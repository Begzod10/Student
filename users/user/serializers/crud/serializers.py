from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from organizations.models.organization_landing_page import OrganizationLandingPage
from students.models import Region
from students.models.student import StudentRequest, Student
from users.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(),
                                                write_only=True)
    landing = serializers.CharField(write_only=True, required=False, allow_null=True,
                                    allow_blank=True)  # Ensure region is processed correctly

    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):

        password = validated_data.pop('password')
        region = validated_data.pop('region', None)  # ✅ Remove region before creating Users
        role = validated_data.get('role', 'user')
        landing = validated_data.pop('landing', None)
        exist_phone = Users.objects.filter(phone=validated_data['phone']).exists()

        if exist_phone:
            return {"phone": "Bu telefon raqamdan foydalanuvchi bor", "status": False}
        user = Users.objects.create(**validated_data)  # ✅ No unexpected keyword arguments now
        user.set_password(password)
        user.save()

        if role == 'user' and region:  # ✅ Ensure region is not None
            Student.objects.create(user=user, region=region)  # ✅ Assign region to Student
        if user.passport_seria and user.passport_number and user.passport_pdf1 and user.passport_pdf2:
            if landing:
                landing_page = get_object_or_404(OrganizationLandingPage, id=landing)
                student = get_object_or_404(Student, user=user)

                if StudentRequest.objects.filter(
                        student=student,
                        organization=landing_page.organization,
                        # shift=landing_page.shift,
                        field=landing_page.field,
                        # language=landing_page.education_language,
                        year=landing_page.year,
                        degree=landing_page.degree,
                        landing_page=landing_page,
                ).exists():
                    raise serializers.ValidationError(
                        {"detail": "Siz allaqachon bu yo'nalishdan ro'yhatdan o'tgansiz!"})

                obj = StudentRequest.objects.create(
                    student=student,
                    organization=landing_page.organization,
                    # shift=landing_page.shift,
                    field=landing_page.field,
                    # language=landing_page.education_language,
                    year=landing_page.year,
                    degree=landing_page.degree,
                    landing_page=landing_page,
                )

                return {"detail": "Arizangiz topshirildi!"}
        else:
            return {"detail": "Profil malumotlari yetarli emas!", "status": False}

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
