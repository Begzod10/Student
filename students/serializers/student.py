from rest_framework import serializers
from students.models.student import StudentRequest


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
    shift = serializers.CharField(source="shift.name")
    language = serializers.CharField(source="language.name")
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


class StudentRequestSerializerList(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    phone = serializers.CharField(source="student.user.phone")
    degree = serializers.CharField(source="degree.name")
    field = serializers.CharField(source="field.name")
    shift = serializers.CharField(source="shift.name")
    language = serializers.CharField(source="language.name")
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