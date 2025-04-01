import django_filters
from test.models.models import Test


class TestFilter(django_filters.FilterSet):
    class Meta:
        model = Test
        fields = {
            'subject': ['exact'],
            'field': ['exact'],
        }
