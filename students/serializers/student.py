from rest_framework import serializers
from students.models.student import StudentRequest
from education.education.serializers.get.retriviev import EducationSerializer
from students.shift.serializers.get.retriviev import ShiftSerializer
from organizations.models.organization_landing_page import OrganizationLandingPage


class StudentRequestSerializerRetrieve(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    phone = serializers.CharField(source="student.user.phone")
    phone_extra = serializers.CharField(source="student.user.phone_extra")
    email = serializers.CharField(source="student.user.email")
    passport_seria = serializers.CharField(source="student.user.passport_seria")
    sex = serializers.CharField(source="student.user.sex")
    indefikatsiya_pin = serializers.CharField(source="student.user.indefikatsiya_pin")
    born_address = serializers.CharField(source="student.user.born_address")
    born_date = serializers.CharField(source="student.user.born_date")
    degree = serializers.CharField(source="degree.name")
    field = serializers.CharField(source="field.name")
    shift = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    organization_name = serializers.SerializerMethodField()
    organization_region = serializers.SerializerMethodField()

    class Meta:
        model = StudentRequest
        fields = [
            'id',
            'name',
            'phone',
            'phone_extra',
            'email',
            'passport_seria',
            'sex',
            'indefikatsiya_pin',
            'born_address',
            'born_date',
            'degree',
            'field',
            'shift',
            'language',
            'date',
            'organization_name',
            'organization_region',
        ]

    def get_name(self, object):
        return f"{object.student.user.name} {object.student.user.surname}"

    def get_organization_name(self, object):
        return {object.organization.name}

    def get_organization_region(self, object):
        return {object.organization.region.name}

    def get_date(self, obj):
        return obj.date.strftime('%Y-%m-%d') if obj.date else None

    def get_language(self, obj):
        landig = OrganizationLandingPage.objects.filter(organization=obj.organization).first()
        return [EducationSerializer(i).data for i in landig.education_language.all()] if landig else []

    def get_shift(self, obj):
        landig = OrganizationLandingPage.objects.filter(organization=obj.organization).first()
        return [ShiftSerializer(i).data for i in landig.shift.all()] if landig else []


class StudentRequestSerializerList(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    phone = serializers.CharField(source="student.user.phone")
    degree = serializers.CharField(source="degree.name")
    field = serializers.CharField(source="field.name")
    shift = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = StudentRequest
        fields = [
            'id',
            'name',
            'phone',
            'degree',
            'field',
            'shift',
            'language',
            'date',
        ]

    def get_name(self, obj):
        return f"{obj.student.user.name} {obj.student.user.surname}"

    def get_date(self, obj):
        return obj.date.strftime('%Y-%m-%d') if obj.date else None

    def get_language(self, obj):
        landig = OrganizationLandingPage.objects.filter(organization=obj.organization).first()
        return [EducationSerializer(i).data for i in landig.education_language.all()] if landig else []

    def get_shift(self, obj):
        landig = OrganizationLandingPage.objects.filter(organization=obj.organization).first()
        return [ShiftSerializer(i).data for i in landig.shift.all()] if landig else []
