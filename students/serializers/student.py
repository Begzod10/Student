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

    class Meta:
        model = StudentRequest
        fields = [
            'id',
            'name'
            'phone'
            'phone_extra'
            'email'
            'passport_seria'
            'sex'
            'indefikatsiya_pin'
            'born_address'
            'born_date'
        ]

    def get_name(self, object):
        return f"{object.student.user.name} {object.student.user.surname}"


class StudentRequestSerializerList(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    phone = serializers.CharField(source="student.user.phone")

    class Meta:
        model = StudentRequest
        fields = [
            'id',
            'name'
            'phone'
        ]

    def get_name(self, object):
        return f"{object.student.user.name} {object.student.user.surname}"
