from django.db.models import Min, Max
from rest_framework import serializers

from organizations.models.models import Organization
from organizations.models.models import OrganizationGallery
from organizations.models.organization_landing_page import OrganizationAdvantage, OrganizationLandingPage
from organizations.organization_type.serializers.get.list import OrganizationTypeSerializerList
from students.academic_year.functions.register_academic_year import register_academic_year
from students.region.serializers.get.retrieve_view import RegionSerializer, DistrictSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    district = DistrictSerializer()
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
            'request_count',
            'instagram_link',
            'facebook_link',
            'telegram_link',
            'youtube_link',
            'website_link',
            'address',
            'email',
            'district'
        ]

    def get_request_count(self, obj):
        register_academic_year()
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
    # desc = serializers.SerializerMethodField()
    # organization_type = serializers.CharField(source='organization_type.name', read_only=True)
    # organization_type_id = serializers.IntegerField(source='organization_type.id', read_only=True)
    # advantages = serializers.SerializerMethodField()
    landing = serializers.SerializerMethodField()
    access_date = serializers.SerializerMethodField()

    # degree = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'locations',
            'desc',
            'desc_json',
            # 'phone',
            'img',
            'organization_type',
            'rating',
            # 'organization_type_id',
            'region',
            # 'advantages',
            'landing',
            'access_date',
            # 'degree'
        ]

    def get_access_date(self, obj):
        landing_qs = OrganizationLandingPage.objects.filter(organization=obj, deleted=False)
        return landing_qs.first().expire_date.strftime('%d.%m.%Y') if landing_qs.exists() else None

    def get_landing(self, obj):
        register_academic_year()

        landing_qs = OrganizationLandingPage.objects.filter(organization=obj, deleted=False)
        landing = landing_qs.first()
        price_stats = landing_qs.aggregate(
            min_sum=Min('price'),
            max_sum=Max('price')
        )
        if landing:
            data = {
                'id': landing.id,
                'shift': [shift.name for shift in landing.shift.all()],
                'price': landing.price,
                'price_min': price_stats['min_sum'],
                'price_max': price_stats['max_sum'],
                'requirements': landing.requirements,
                'language': [lang.name for lang in landing.education_language.all()],
                'grant': landing.grant,
            }
            return data
        return None

    def get_degree(self, obj):
        register_academic_year()
        obj = OrganizationLandingPage.objects.filter(organization=obj, deleted=False).distinct()
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
            'type',
            'desc_json',
            'grand_text',
            'grand_json',
            'inn',
            'img',
            'name',
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
    img = serializers.CharField(source='organization.img')
    field = serializers.SerializerMethodField()

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
            'start_date',
            'expire_date',
            'desc_json',
            'img',
            'field'
        ]

    def get_type(self, obj):
        if obj.organization.organization_type.name == 'Universitet':
            return obj.requirements or None
        else:
            return obj.degree.name or None

    def get_field(self, obj):
        data = {
            'id': obj.field.id,
            'name': obj.field.name,
            'desc': obj.field.desc
        }
        return data
