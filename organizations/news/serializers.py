import re

from rest_framework import serializers

from ..models.news import News, NewsView, NewsBlock
from ..models.organization_landing_page import OrganizationLandingPage


class NewsSerializer(serializers.ModelSerializer):
    views_display = serializers.SerializerMethodField()
    shared = serializers.SerializerMethodField()
    landing = serializers.SerializerMethodField(allow_null=True, required=False, read_only=True)
    visitor_id = serializers.SerializerMethodField()
    desc_json = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'deleted', 'views_display', 'shared', 'landing', 'desc_json',
                  'visitor_id', 'organization']

    def get_views_display(self, obj):
        view_count = NewsView.objects.filter(news=obj).count()
        if view_count >= 1000:
            return f"{view_count / 1000:.1f}K views"
        return f"{view_count} views"

    def get_desc_json(self, obj):
        return obj.news_block[0].desc_json if obj.news_block else None

    def get_landing(self, obj):
        extra_details = []

        view = self.context.get('view')
        if view and hasattr(view, 'action') and view.action == 'retrieve':  # <- safer
            try:
                org = obj.organization
                org_landing = OrganizationLandingPage.objects.filter(
                    organization=org, deleted=False
                ).order_by('-start_date').all()
                if org_landing:
                    for landing in org_landing:
                        extra_details.append({
                            'id': landing.id,
                            'start_date': landing.start_date,
                            'expired_date': landing.expire_date,
                            'shift': landing.shift.name,
                            'price': landing.price if landing else None,
                            'degree': landing.degree.name,
                            'field': landing.field.name if landing.field else None,
                            'requirements': landing.requirements,
                            'language': landing.education_language.name if landing.education_language else None,
                            'grant': landing.grant,
                            'desc': landing.desc,
                            'desc_json': landing.desc_json
                        })
            except (AttributeError, OrganizationLandingPage.DoesNotExist):
                pass
        return extra_details

    def get_shared(self, obj):
        base_url = self.context.get('request').build_absolute_uri('/')
        news_url = f"{base_url}news/{obj.id}"

        desc_text = ""
        if obj.news_block[0].desc_json and 'text' in obj.news_block[0].desc_json:
            full_text = obj.news_block[0].desc_json['text']
            clean_text = re.sub(r'<[^>]+>', '', full_text)
            period_index = clean_text.find('.')
            desc_text = clean_text[:period_index + 1] if period_index != -1 else clean_text

        share_text = f"{desc_text or obj.title}"

        return {
            "telegram": f"https://telegram.me/share/url?url={news_url}&text={share_text}",
            "facebook": f"https://www.facebook.com/sharer/sharer.php?u={news_url}",
            "twitter": f"https://twitter.com/intent/tweet?text={share_text}&url={news_url}",
            "instagram": f"https://www.instagram.com/?url={news_url}",
        }

    def get_visitor_id(self, obj):
        # Requestdan visitor_id ni olish
        return self.context.get('visitor_id')


class NewsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBlock
        fields = ['id', 'desc_json', 'img', 'news']

    def create(self, validated_data):
        last_block = NewsBlock.objects.filter(news=validated_data['news']).order_by('-index').first()
        if last_block:
            validated_data['index'] = last_block.index + 1
        return NewsBlock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
