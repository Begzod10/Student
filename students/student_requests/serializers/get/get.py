from rest_framework import serializers

from students.models.student import StudentRequest


class StudentRequestProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    language = serializers.CharField()
    date = serializers.DateField()

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'user': {
                'name': f'{obj.student.user.name} {obj.student.user.surname or ""} {obj.student.user.last_name or ""}'.strip(),
                'phone': obj.student.user.phone,
                'phone_extra': obj.student.user.phone_extra or "N/A",
                'email': obj.student.user.email
            },
            'request': {
                'degree': obj.degree.name,
                'shift': obj.shift.name,
                'language': obj.language.name
            },
            'passport': {
                'seria': obj.student.user.passport_seria,
                'born_date': obj.student.user.born_date,
                'identification_pin': obj.student.user.indefikatsiya_pin,
                'sex': obj.student.user.sex,
                'born_address': obj.student.user.born_address
            },
            'organizations': {
                'name': obj.organization.name,
                'locations': obj.organization.locations,
                'desc': obj.organization.desc,
                'phone': obj.organization.phone,
                'organization_type': obj.organization.organization_type.name,
                'region': obj.organization.region.name
            },
            'language': obj.language.name,
            'date': obj.date
        }


class StudentRequestListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    phone = serializers.CharField(source='student.user.phone')
    degree = serializers.CharField(source='degree.name')
    shift = serializers.CharField(source='shift.name')
    language = serializers.CharField(source='language.name')
    field = serializers.CharField(source='field.name')

    # direction ta'lim yo'nalishi xali qoshilmadi

    class Meta:
        model = StudentRequest
        fields = ['id', 'name', 'phone', 'degree', 'shift', 'language', 'date', 'accepted', 'field']

    def get_name(self, obj):
        name_parts = []

        if obj.student.user.name:
            name_parts.append(obj.student.user.name)
        if obj.student.user.surname:
            name_parts.append(obj.student.user.surname)
        if obj.student.user.last_name:
            name_parts.append(obj.student.user.last_name)

        return ' '.join(name_parts)


class StudentRequestProfileSerializers(serializers.ModelSerializer):
    degree = serializers.CharField(source='degree.name')
    language = serializers.CharField(source='language.name')
    shift = serializers.CharField(source='shift.name')
    price = serializers.CharField(source='landing_page.price')
    region = serializers.CharField(source='organization.region.name')
    location = serializers.CharField(source='organization.locations')
    name = serializers.CharField(source='organization.name')

    class Meta:
        model = StudentRequest
        fields = [
            'id', 'degree', 'language', 'shift', 'location', 'name',
            'price', 'region', 'accepted', 'canceled', 'back_recovery',
            'called_to_exam', 'present_in_exam', 'evaluated',
            'contract_given', 'payed_status', 'accepted_to_study',
            'request_status', 'date'
        ]
