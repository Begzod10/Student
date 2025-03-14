from rest_framework import serializers

from organizations.models.models import Organization
from organizations.models.models import OrganizationGallery
from organizations.models.organization_landing_page import OrganizationAdvantage, OrganizationLandingPage
from organizations.organization_type.serializers.get.list import OrganizationTypeSerializerList
from students.academic_year.functions.register_academic_year import register_academic_year
from students.region.serializers.get.retrieve_view import RegionSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    organization_type = OrganizationTypeSerializerList()
    request_count = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'locations',
            'desc',
            'phone',
            'img',
            'organization_type',
            'region',
            'desc_json',
            'grand_text',
            "grand_json",
            'inn',
            'request_count'
        ]

    def get_request_count(self, obj):
        from students.models.student import StudentRequest
        count = StudentRequest.objects.filter(organization=obj).count()
        return count


class OrganizationSerializerForLanding(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name'
        ]


class OrganizationGrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'grand_text',
            'grand_json'
        ]


class OrganizationDescUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'desc',
            'desc_json'
        ]


class OrganizationHomeSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='region.name', read_only=True)
    desc = serializers.SerializerMethodField()
    organization_type = serializers.CharField(source='organization_type.name', read_only=True)
    organization_type_id = serializers.IntegerField(source='organization_type.id', read_only=True)
    advantages = serializers.SerializerMethodField()
    landing = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'locations',
            'desc',
            'phone',
            'img',
            'organization_type',
            'organization_type_id',
            'region',
            'advantages',
            'landing',
            'degree'
        ]

    def get_landing(self, obj):
        register_academic_year()
        obj = OrganizationLandingPage.objects.filter(organization=obj).first()
        if obj:
            data = {
                'id': obj.id,
                'start_date': obj.start_date,
                'expired_date': obj.expire_date,
                'education_language': obj.education_language.name,
                'shift': obj.shift.name,
                'price': obj.price if obj else None,
                'degree': obj.degree.name,
                'field': obj.field.name if obj.field else None,
                'requirements': obj.requirements,
                'language': obj.education_language.name if obj.education_language else None,
                'grant': obj.grant,
                'desc': obj.desc,
                'desc_json': obj.desc_json
            }
            return data

    def get_degree(self, obj):
        register_academic_year()
        obj = OrganizationLandingPage.objects.filter(organization=obj).distinct()
        data_dict = {}

        for i in obj:
            if i.degree.name not in data_dict:
                data_dict[i.degree.name] = {
                    'id': i.degree.id,
                    'name': i.degree.name
                }

        data = sorted(data_dict.values(), key=lambda x: x['name'])

        return data

    def get_desc(self, obj):
        register_academic_year()
        if obj.desc:
            return f"{obj.desc[:500]}..."

    def get_advantages(self, obj):
        register_academic_year()
        text = OrganizationAdvantage.objects.filter(organization=obj).first()
        if text:
            if text.desc:
                return f"{text.desc[:500]}..."


class OrganizationDescSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='organization_type.name', read_only=True)

    class Meta:
        model = Organization
        fields = [
            'id',
            'desc',
            'type'
        ]


class OrganizationAdvantagesSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='organization.organization_type.name', read_only=True)
    file = serializers.CharField(source='file.url', read_only=True)

    class Meta:
        model = OrganizationAdvantage
        fields = [
            'id',
            'desc',
            'type',
            'name_optional',
            'file'
        ]


class OrganizationGallerySerializer(serializers.ModelSerializer):
    file = serializers.CharField(source='file.url.url', read_only=True)

    class Meta:
        model = OrganizationGallery
        ref_name = 'OrganizationGalleryDetail'
        fields = [
            'id',
            'file'
        ]


class OrganizationOrganizationLandingPageSerializer(serializers.ModelSerializer):
    education_language = serializers.CharField(source='education_language.name')
    shift = serializers.CharField(source='shift.name')
    type = serializers.SerializerMethodField()
    name = serializers.CharField(source='organization.name')
    region = serializers.CharField(source='organization.region.name')

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'education_language',
            'shift',
            'price',
            'type',
            'name',
            'region'
        ]

    def get_type(self, obj):
        if obj.organization.organization_type.name == 'Universitet':
            return obj.requirements or None
        else:
            return obj.degree.name or None


class OrganizationOrganizationLandingPageSerializer2(serializers.ModelSerializer):
    education_language = serializers.CharField(source='education_language.name')
    shift = serializers.CharField(source='shift.name')
    type = serializers.SerializerMethodField()
    name = serializers.CharField(source='organization.name')
    region = serializers.CharField(source='organization.region.name')
    grand = serializers.CharField(source='organization.grand_text')
    location = serializers.CharField(source='organization.locations')

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'education_language',
            'shift',
            'price',
            'type',
            'name',
            'region',
            'grand',
            'location',
            'start_date'
        ]

    def get_type(self, obj):
        if obj.organization.organization_type.name == 'Universitet':
            return obj.requirements or None
        else:
            return obj.degree.name or None
