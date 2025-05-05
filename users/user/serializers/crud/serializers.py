from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from organizations.models.organization_landing_page import OrganizationLandingPage
from students.models import Region
from students.models.student import StudentRequest, Student
from users.models import Users


def retrieve(instance):
    return instance


class RegisterSerializer(serializers.ModelSerializer):
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(),
                                                write_only=True)
    landing = serializers.CharField(write_only=True, required=False, allow_null=True,
                                    allow_blank=True)  # Ensure region is processed correctly
    image = serializers.ImageField(required=False, allow_null=True)
    passport_pdf1 = serializers.FileField(required=False, allow_null=True)
    passport_pdf2 = serializers.FileField(required=False, allow_null=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'phone', 'region', 'landing', 'phone_extra',
                  'email', 'image', 'passport_seria', 'passport_number', 'passport_pdf1', 'passport_pdf2',
                  'indefikatsiya_pin', 'certificate', 'password', 'born_address', 'born_date', 'sex']
        # extra_kwargs = {
        #     'password': {'write_only': True},  # Ensure password is write-only
        # }

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        # instance.username = validated_data.get('username', instance.username)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.phone_extra = validated_data.get('phone_extra', instance.phone_extra)
        instance.email = validated_data.get('email', instance.email)
        # instance.file = validated_data.get('file', instance.file)
        instance.certificate = validated_data.get('certificate', instance.certificate)
        instance.image = validated_data.get('image', instance.image)
        instance.passport_seria = validated_data.get('passport_seria', instance.passport_seria)
        instance.passport_number = validated_data.get('passport_number', instance.passport_number)
        instance.passport_pdf1 = validated_data.get('passport_pdf1', instance.passport_pdf1)
        instance.passport_pdf2 = validated_data.get('passport_pdf2', instance.passport_pdf2)
        instance.indefikatsiya_pin = validated_data.get('indefikatsiya_pin', instance.indefikatsiya_pin)
        instance.password = validated_data.get('password', instance.password)
        instance.born_address = validated_data.get('born_address', instance.born_address)
        instance.born_date = validated_data.get('born_date', instance.born_date)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.save()
        return instance

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
        if user.passport_seria  and user.passport_pdf1 and user.passport_pdf2 and user.name and user.surname:
            if landing:
                landing_page = get_object_or_404(OrganizationLandingPage, id=landing)
                student = get_object_or_404(Student, user=user)

                if StudentRequest.objects.filter(
                        student=student,
                        # organization=landing_page.organization,
                        # shift=landing_page.shift,
                        field=landing_page.field,
                        # language=landing_page.education_language,
                        # year=landing_page.year,
                        # degree=landing_page.degree,
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
