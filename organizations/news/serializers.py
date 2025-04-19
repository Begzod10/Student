import re

from rest_framework import serializers

from ..models.news import News, NewsView
from ..models.organization_landing_page import OrganizationLandingPage


class NewsSerializer(serializers.ModelSerializer):
    views_display = serializers.SerializerMethodField()
    shared = serializers.SerializerMethodField()
    landing = serializers.SerializerMethodField(allow_null=True, required=False, read_only=True)
    visitor_id = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'desc_json', 'img', 'date', 'deleted', 'views_display', 'shared', 'landing',
                  'visitor_id', 'organization']

    def get_views_display(self, obj):
        view_count = NewsView.objects.filter(news=obj).count()
        if view_count >= 1000:
            return f"{view_count / 1000:.1f}K views"
        return f"{view_count} views"

    def get_landing(self, obj):
        extra_details = []

        if self.context.get('view') and self.context['view'].action == 'retrieve':
            try:
                org = obj.organization
                org_landing = OrganizationLandingPage.objects.filter(organization=org,deleted=False).order_by('-start_date').all()
                if org_landing:

                    for org_landing in org_landing:
                        extra_details.append({
                            'id': org_landing.id,
                            'start_date': org_landing.start_date,
                            'expired_date': org_landing.expire_date,
                            'shift': org_landing.shift.name,
                            'price': org_landing.price if org_landing else None,
                            'degree': org_landing.degree.name,
                            'field': org_landing.field.name if org_landing.field else None,
                            'requirements': org_landing.requirements,
                            'language': org_landing.education_language.name if org_landing.education_language else None,
                            'grant': org_landing.grant,
                            'desc': org_landing.desc,
                            'desc_json': org_landing.desc_json
                        })
                        ''

            except (AttributeError, OrganizationLandingPage.DoesNotExist):
                pass
        return extra_details

    def get_shared(self, obj):
        base_url = self.context.get('request').build_absolute_uri('/')
        news_url = f"{base_url}news/{obj.id}"

        desc_text = ""
        if obj.desc_json and 'text' in obj.desc_json:
            full_text = obj.desc_json['text']
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
