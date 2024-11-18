import django_filters
from students.models.student import StudentRequest


class StudentRequestFilter(django_filters.FilterSet):
    type_id = django_filters.NumberFilter(field_name="organization__organization_type_id")

    class Meta:
        model = StudentRequest
        fields = ['degree_id', 'language_id', 'type_id']
