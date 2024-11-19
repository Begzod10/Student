import django_filters
from students.models.student import StudentRequest


class StudentRequestFilter(django_filters.FilterSet):
    type_id = django_filters.NumberFilter(field_name="organization__organization_type_id")

    degree_id = django_filters.NumberFilter(field_name="degree_id")
    language_id = django_filters.NumberFilter(field_name="language_id")
    shift_id = django_filters.NumberFilter(field_name="shift_id")
    field_id = django_filters.NumberFilter(field_name="field_id")

    class Meta:
        model = StudentRequest
        fields = ['degree_id', 'language_id', 'type_id', 'shift_id', 'field_id']
