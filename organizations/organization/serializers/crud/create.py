from rest_framework import serializers
from organizations.models.models import Organization


class OrganizationCreateSerializer(serializers.ModelSerializer):


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
            'inn',
            'instagram_link',
            'facebook_link',
            'telegram_link',
            'youtube_link',
            'website_link',
            'address',
            'email'
        ]
